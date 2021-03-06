/**
 * Created by syariefa on 2/27/16.
 */
$(document).ready(function(){
    var url = '/monitor/realtime/';
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    $('div#rltm_kec_angin').highcharts({
        chart: {
            type: 'area',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
            events: {
                load: function () {

                    // set up the updating of the chart each second
                    var series = this.series[0];
                    setInterval(function () {
                        var x = (new Date()).getTime(), y;

                        $.get(url+'kec/'+x, function(val_kec){
                            if(val_kec.length > 0)
                            {
                                y = val_kec[0].fields.kecepatan;
                            }

                            else
                            {
                                y = 0;
                            }

                            series.addPoint([x, y], true, true);
                        });
                    }, 3000);
                }
            }
        },
        title: {
            text: 'Grafik Perubahan Kecepatan Angin'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150
        },
        yAxis: {
            title: {
                text: 'Kecepatan Angin (m/s)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                    Highcharts.numberFormat(this.y, 2);
            }
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        series: [{
            name: 'Data Kecepatan Angin',
            data: (function () {
                var data = [];
                var dt_x_selector = $("div#wkt span");
                var dt_y_selector = $("div#kec span");
                var dt_x = 0;
                var dt_y = 0;

                dt_x_selector.each(function(){
                    dt_x = $(this).text();
                    dt_y_selector.each(function(){
                        dt_y = $(this).text();
                    });

                    data.push({
                        x: parseInt(dt_x),
                        y: parseInt(dt_y)
                    });
                });
                return data;
            }())
        }]
    });

//--------------------------------------------------
    $('div#rltm_arh_angin').highcharts({
        chart: {
            type: 'area',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
            events: {
                load: function () {

                    // set up the updating of the chart each second
                    var series = this.series[0];
                    setInterval(function () {
                        var x = (new Date()).getTime(), // current time
                            y;
                        $.get(url+'arh/'+x, function(val_arh){
                            if(val_arh.length > 0)
                            {
                                y = val_arh[0].fields.arah;
                            }

                            else
                            {
                                y = 0;
                            }

                            series.addPoint([x, y], true, true);
                        });
                    }, 3000);
                }
            }
        },
        title: {
            text: 'Grafik Perubahan Arah Angin'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150
        },
        yAxis: {
            title: {
                text: 'Arah Angin (derajat)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                    Highcharts.numberFormat(this.y, 2);
            }
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        series: [{
            name: 'Data Arah Angin',
            data: (function () {
                var data = [];
                var dt_x_selector = $("div#wkt span");
                var dt_y_selector = $("div#arh span");
                var dt_x = 0;
                var dt_y = 0;

                dt_x_selector.each(function(){
                    dt_x = $(this).text();
                    dt_y_selector.each(function(){
                        dt_y = $(this).text();
                    });

                    data.push({
                        x: parseInt(dt_x),
                        y: parseInt(dt_y)
                    });
                });
                return data;
            }())
        }]
    });

//-------------------------------------------------------
    $('div#rltm_gtr_angin').highcharts({
        chart: {
            type: 'area',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
            events: {
                load: function () {

                    // set up the updating of the chart each second
                    var series = this.series[0];
                    setInterval(function () {
                        var x = (new Date()).getTime(), // current time
                            y;
                        $.get(url+'gtr/'+x, function(val_acc){
                            if(val_acc.length > 0)
                            {
                                y = val_acc[0].fields.akselerator5;
                            }

                            else
                            {
                                y = 0;
                            }

                            series.addPoint([x, y], true, true);
                        });
                    }, 3000);
                }
            }
        },
        title: {
            text: 'Grafik Perubahan Getaran Akibat Angin'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150
        },
        yAxis: {
            title: {
                text: 'Getaran (m/s2)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                    Highcharts.numberFormat(this.y, 2);
            }
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        series: [{
            name: 'Data Getaran Akibat Angin',
            data: (function () {
                var data = [];
                var dt_x_selector = $("div#wkt span");
                var dt_y_selector = $("div#gtr span");
                var dt_x = 0;
                var dt_y = 0;

                dt_x_selector.each(function(){
                    dt_x = $(this).text();
                    dt_y_selector.each(function(){
                        dt_y = $(this).text();
                    });

                    data.push({
                        x: parseInt(dt_x),
                        y: parseInt(dt_y)
                    });
                });
                return data;
            }())
        }]
    });
});