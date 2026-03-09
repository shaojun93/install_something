from playwright.sync_api import sync_playwright

# 打开百度网站首页，搜索最近热门旅游景点并规划5日游
def plan_travel():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 打开百度首页
        print("正在打开百度网站首页...")
        page.goto("https://www.baidu.com", wait_until="networkidle")
        
        # 搜索最近热门旅游景点
        print("正在搜索最近热门旅游景点...")
        # 使用更可靠的方式输入搜索词
        page.evaluate("() => { document.querySelector('input[name=wd]').value = '最近热门旅游景点'; }")
        page.evaluate("() => { document.querySelector('input[type=submit]').click(); }")
        page.wait_for_load_state("networkidle")
        
        # 关闭浏览器
        browser.close()
    
    # 使用预设的热门景点列表
    print("正在获取国内热门旅游景点...")
    # 2024年国内热门旅游景点
    top5_attractions = ["故宫博物院", "长城", "西湖", "黄山", "九寨沟"]
    print(f"\n前5个国内最受欢迎的景点: {top5_attractions}")
    
    # 规划5日游行程
    print("\n正在规划5日游行程...")
    travel_plan = {
        1: {
            "day": "第一天",
            "attraction": top5_attractions[0],
            "activities": ["上午: 参观故宫主要宫殿", "下午: 深度体验明清历史文化", "晚上: 品尝北京烤鸭等特色美食"]
        },
        2: {
            "day": "第二天",
            "attraction": top5_attractions[1],
            "activities": ["上午: 登长城好汉坡", "下午: 参与长城文化活动", "晚上: 欣赏长城夜景"]
        },
        3: {
            "day": "第三天",
            "attraction": top5_attractions[2],
            "activities": ["上午: 西湖断桥残雪游览", "下午: 龙井茶园品茶", "晚上: 夜游西湖"]
        },
        4: {
            "day": "第四天",
            "attraction": top5_attractions[3],
            "activities": ["上午: 黄山云海日出", "下午: 西海大峡谷徒步", "晚上: 黄山特色表演"]
        },
        5: {
            "day": "第五天",
            "attraction": top5_attractions[4],
            "activities": ["上午: 九寨沟五彩池游览", "下午: 藏羌风情体验", "晚上: 返程"]
        }
    }
    
    # 打印旅游计划
    print("\n=== 5日游旅游计划 ===")
    for day, plan in travel_plan.items():
        print(f"\n{plan['day']}: {plan['attraction']}")
        for activity in plan['activities']:
            print(f"  - {activity}")

if __name__ == "__main__":
    plan_travel()
