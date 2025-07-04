#!/usr/bin/env python3
"""
Direct browser control without nested LLM.
This module provides browser automation that returns screenshots and page info
for the calling agent to analyze and decide next actions.
"""

import asyncio
import base64
from typing import List, Dict, Any
from playwright.async_api import async_playwright, Page, Browser
from mcp.types import TextContent, ImageContent

class DirectBrowserController:
    """Controls browser directly without nested LLM"""
    
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
    
    async def setup(self, headless: bool = True):
        """Initialize browser"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=headless,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        self.context = await self.browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        self.page = await self.context.new_page()
    
    async def navigate(self, url: str) -> Dict[str, Any]:
        """Navigate to URL and return page info"""
        await self.page.goto(url, wait_until='networkidle')
        return await self.get_page_state()
    
    async def click(self, selector: str) -> Dict[str, Any]:
        """Click element and return new state"""
        await self.page.click(selector)
        await self.page.wait_for_load_state('networkidle')
        return await self.get_page_state()
    
    async def type_text(self, selector: str, text: str) -> Dict[str, Any]:
        """Type text in input field"""
        await self.page.fill(selector, text)
        return await self.get_page_state()
    
    async def get_page_state(self) -> Dict[str, Any]:
        """Get current page state including screenshot"""
        # Take screenshot
        screenshot_bytes = await self.page.screenshot(type="jpeg", quality=80)
        screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        
        # Get page info
        title = await self.page.title()
        url = self.page.url
        
        # Get visible text
        text_content = await self.page.evaluate("""
            () => {
                const walker = document.createTreeWalker(
                    document.body,
                    NodeFilter.SHOW_TEXT,
                    null,
                    false
                );
                const text = [];
                let node;
                while (node = walker.nextNode()) {
                    const content = node.textContent.trim();
                    if (content) text.push(content);
                }
                return text.join(' ').slice(0, 5000); // Limit text length
            }
        """)
        
        # Get interactive elements
        elements = await self.page.evaluate("""
            () => {
                const selectors = [];
                // Buttons
                document.querySelectorAll('button').forEach((el, i) => {
                    if (el.offsetParent !== null) {
                        selectors.push({
                            type: 'button',
                            selector: `button:nth-of-type(${i+1})`,
                            text: el.textContent.trim().slice(0, 50)
                        });
                    }
                });
                // Links
                document.querySelectorAll('a[href]').forEach((el, i) => {
                    if (el.offsetParent !== null) {
                        selectors.push({
                            type: 'link',
                            selector: `a:nth-of-type(${i+1})`,
                            text: el.textContent.trim().slice(0, 50),
                            href: el.href
                        });
                    }
                });
                // Inputs
                document.querySelectorAll('input, textarea').forEach((el, i) => {
                    if (el.offsetParent !== null) {
                        selectors.push({
                            type: el.type || 'text',
                            selector: `${el.tagName.toLowerCase()}:nth-of-type(${i+1})`,
                            placeholder: el.placeholder || '',
                            name: el.name || ''
                        });
                    }
                });
                return selectors.slice(0, 50); // Limit number of elements
            }
        """)
        
        return {
            'screenshot': screenshot_base64,
            'title': title,
            'url': url,
            'text_preview': text_content[:1000],
            'interactive_elements': elements
        }
    
    async def cleanup(self):
        """Clean up browser resources"""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

async def evaluate_web_direct(url: str, task: str, headless: bool = True) -> Dict[str, Any]:
    """
    Direct browser control that returns state for the calling agent to analyze.
    No nested LLM required - the calling agent decides all actions.
    """
    controller = DirectBrowserController()
    results = []
    
    try:
        await controller.setup(headless=headless)
        
        # Initial navigation
        state = await controller.navigate(url)
        
        results.append(TextContent(
            type="text",
            text=f"Navigated to {url}\nTitle: {state['title']}\n\nTask: {task}\n\nPage has {len(state['interactive_elements'])} interactive elements.\n\nVisible text preview:\n{state['text_preview'][:500]}...\n\nYou can interact with the page by requesting specific actions like:\n- Click on button/link (provide selector)\n- Type in input field (provide selector and text)\n- Navigate to URL\n\nInteractive elements found:\n" + 
            "\n".join([f"- {el['type']}: {el.get('text', el.get('placeholder', ''))} [{el.get('selector', '')}]" for el in state['interactive_elements'][:10]])
        ))
        
        results.append(ImageContent(
            type="image",
            data=state['screenshot'],
            mimeType="image/jpeg"
        ))
        
        # Store controller reference for potential follow-up actions
        # In a real implementation, you'd manage this session properly
        
    except Exception as e:
        results.append(TextContent(
            type="text",
            text=f"Error during browser automation: {str(e)}"
        ))
    finally:
        await controller.cleanup()
    
    return {
        "result": results,
        "screenshot_storage": [{"screenshot": state['screenshot'], "url": url}] if 'state' in locals() else []
    }