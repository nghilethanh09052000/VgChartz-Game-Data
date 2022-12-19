const Crawler = require("crawler");
const _ = require('lodash');


const c = new Crawler({
    maxConnections: 10,
    callback : function (error, res, done) {
        if(error)
        {
            console.log('Error...................................................................')
            console.log(error);
        }
        else
        {
            const $ = res.$;
            console.log('Success.................................................................')
            let rows = $("#generalBody table tr").each((index,row)=>{
                if(row.attribs.style) 
                {
                    pos = row.children

                    console.log(pos)
                }
            })
            //console.log(rows)
        }
        done();
    }
})

const pages = Array.from(Array(1).keys())
const gameUrls = _.map(pages, page => `https://www.vgchartz.com/games/games.php?page=${page}&order=Sales&ownership=Both&direction=DESC&showtotalsales=${page}&shownasales=${page}&showpalsales=${page}&showjapansales=${page}&showothersales=${page}&showpublisher=${page}&showdeveloper=${page}&showreleasedate=${page}&showlastupdate=${page}&showvgchartzscore=${page}&showcriticscore=${page}&showuserscore=${page}&showshipped=${page}`)
_.forEach(gameUrls , gameUrl => c.queue(gameUrl))




