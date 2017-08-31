# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURl = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseURl + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']")

        for node in node_list:
            item = TencentItem()
            item["positionName"] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
            item["positionLink"] = node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
            if (len(node.xpath("./td[2]/text()"))):
                item["positionType"] = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            else:
                item["positionType"] = ""
            item["peopleNumber"] = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            item["workPosition"] = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item["publishTime"] = node.xpath("./td[5]/text()").extract()[0].encode("utf-8")
            yield item
            # if self.offset < 2190:
            #     self.offset += 10
            #     url = self.baseURl + str(self.offset)
            #     yield scrapy.Request(url, callback=self.parse)
        if len(response.xpath("//a[@class='noactive' and @id ='next']")) == 0:
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("http://hr.tencent.com/" + url, callback=self.parse)