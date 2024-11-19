import aiohttp

from bs4 import BeautifulSoup




async def get_links(query: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                items = soup.select("a.s-item__link")
                links = []
                for item in items[:7]:
                    if "/itm/123456?" in item["href"]:
                        pass
                    else:
                        links.append(item["href"])
                print(items)
                print(links)
                return links
            else:
                print(response.status)
                return "Error"