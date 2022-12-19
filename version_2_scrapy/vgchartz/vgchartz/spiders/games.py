import scrapy


class GamesSpider(scrapy.Spider):
    name = 'games'
    allowed_domains = ['www.vgchartz.com']

    def createUrl(n):
        return f"https://www.vgchartz.com/games/games.php?page={n}&order=Sales&ownership=Both&direction=DESC&showtotalsales={n}&shownasales={n}&showpalsales={n}&showjapansales={n}&showothersales={n}&showpublisher={n}&showdeveloper={n}&showreleasedate={n}&showlastupdate={n}&showvgchartzscore={n}&showcriticscore={n}&showuserscore={n}&showshipped={n}/"
    
    page_list = list(range(1, 3))
    start_urls = map(createUrl,page_list)

    def parse(self, response):
        rows = response.xpath('//*[@id="generalBody"]/table[1]')
        # for row in rows:
        #     pos = row.xpath('//td[1]/text()').get()
        #     print(pos)
            # gameName = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[3]/a").get()
            # console = game.xpath('//*[@id="generalBody"]/table[1]/tbody/tr[4]/td[4]/img').get()
            # publisher = game.xpath('//*[@id="generalBody"]/table[1]/tbody/tr[4]/td[5]').get()
            # totalShipped = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # totalSales = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # naSales = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # palSales = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # jpSales = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # otherSales = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # releaseDate = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # lastUpdate = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # chartScore = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # criticScore = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # userScore = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
            # releasedDate = game.xpath("//*[@id='generalBody']/table[1]/tbody/tr[4]/td[1]")
        yield {
            'Row':rows
        }
            # yield {
            #     'Position': pos,
            #     # 'Game': gameName,
            #     # 'Console': console,
            #     # 'Publisher': publisher,
            #     # 'Total Shipped': totalShipped,
            #     # 'Total Sales': totalSales,
            #     # 'NA Sales': naSales,
            #     # 'PAL Sales': palSales,
            #     # 'Japan Sales': jpSales,
            #     # 'Other Sales': otherSales,
            #     # 'Release Date': releaseDate,
            #     # 'Last Update': lastUpdate,
            #     # 'VGChartz Score': chartScore,
            #     # 'Critic Score': criticScore,
            #     # 'User Score': userScore,
            #     # 'Release Date': releasedDate,
            # }
