from playwright.sync_api import sync_playwright
import time

# 打开指定网页并点击所有超链接
def open_and_click_links():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 打开指定网页
        url = "https://docs.trae.com.cn/ide/model-context-protocol"
        print(f"正在打开网页: {url}")
        page.goto(url, wait_until="networkidle")
        
        # 截图：主页面
        timestamp = int(time.time())
        main_screenshot = f"screenshot_main_{timestamp}.png"
        page.screenshot(path=main_screenshot)
        print(f"已保存主页面截图: {main_screenshot}")
        
        # 获取页面上的所有超链接
        links = page.query_selector_all("a[href]")
        print(f"找到 {len(links)} 个超链接")
        
        # 点击每个超链接
        for i, link in enumerate(links):
            try:
                href = link.get_attribute("href")
                if href:
                    # 跳过内部锚点链接
                    if href.startswith("#"):
                        print(f"跳过内部锚点链接 {i+1}: {href}")
                        continue
                    
                    print(f"点击超链接 {i+1}: {href}")
                    # 打开新标签页点击链接
                    with page.context.expect_page() as new_page_info:
                        link.click()
                    new_page = new_page_info.value
                    new_page.wait_for_load_state("networkidle", timeout=10000)
                    print(f"已打开: {new_page.url}")
                    
                    # 截图：打开的页面
                    link_screenshot = f"screenshot_link_{i+1}_{timestamp}.png"
                    new_page.screenshot(path=link_screenshot)
                    print(f"已保存链接页面截图: {link_screenshot}")
                    
                    new_page.close()
            except Exception as e:
                print(f"点击超链接 {i+1} 时出错: {e}")
                continue  # 继续处理下一个链接
        
        # 关闭浏览器
        browser.close()

if __name__ == "__main__":
    open_and_click_links()
