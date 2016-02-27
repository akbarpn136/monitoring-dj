/**
 * Created by syariefa on 2/27/16.
 */
$(document).ready(function(){
    $("input#in_tgl").Zebra_DatePicker({
        show_icon: false,
        onSelect: function(a){
            var inpt = '<div class="ui icon input">';
            inpt += '<input id="in_tgl_akhir" type="text" placeholder="Tanggal akhir">';
            inpt += '<i class="calendar icon"></i>';
            inpt += '</div>';

            $("span#data_tgl_awl").attr("data-value", a);
            $("div#tanggal_akhir").append().html(inpt);
            $("input#in_tgl_akhir").Zebra_DatePicker({
                show_icon: false,
                onClear: function(){
                    $("div#jenis_grafik").empty();
                    $("div#WRS").empty();
                },
                onSelect: function(b){
                    var selector_tgl_akr = $("span#data_tgl_akr");
                    var daerah_tertentu1 = $("span#data_daerah").attr("data-value");
                    var graph1=document.getElementById("WRS");

                    selector_tgl_akr.attr("data-value", b);

                    $("div#loader").addClass('active');

                    $.get('/monitor/' + daerah_tertentu1 + '/rose/' + $("span#data_tgl_awl").attr("data-value") + '/' + selector_tgl_akr.attr("data-value"), function(data){
                        var trace1 = {
                            r: data[0].trace1,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '0-0.5 m/s',
                            marker: {color: 'rgb(0,51,0)'},
                            type: 'area'
                        };

                        var trace2 = {
                            r: data[0].trace2,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '0.5-1 m/s',
                            marker: {color: 'rgb(51,0,0)'},
                            type: 'area'
                        };

                        var trace3 = {
                            r: data[0].trace3,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '1-1.5 m/s',
                            marker: {color: 'rgb(51,51,0)'},
                            type: 'area'
                        };

                        var trace4 = {
                            r: data[0].trace4,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '1.5-2 m/s',
                            marker: {color: 'rgb(102,0,0)'},
                            type: 'area'
                        };

                        var trace5 = {
                            r: data[0].trace5,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '2-2.5 m/s',
                            marker: {color: 'rgb(204,255,0)'},
                            type: 'area'
                        };

                        var trace6 = {
                            r: data[0].trace6,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '2.5-3 m/s',
                            marker: {color: 'rgb(255,153,255)'},
                            type: 'area'
                        };

                        var trace7 = {
                            r: data[0].trace7,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '3-3.5 m/s',
                            marker: {color: 'rgb(204,255,255)'},
                            type: 'area'
                        };

                        var trace8 = {
                            r: data[0].trace8,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '3.5-4 m/s',
                            marker: {color: 'rgb(102,102,255)'},
                            type: 'area'
                        };

                        var trace9 = {
                            r: data[0].trace9,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '4-4.5 m/s',
                            marker: {color: 'rgb(121,189,143)'},
                            type: 'area'
                        };

                        var trace10 = {
                            r: data[0].trace10,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '4.5-5 m/s',
                            marker: {color: 'rgb(0,163,136)'},
                            type: 'area'
                        };

                        var trace11 = {
                            r: data[0].trace11,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '5-5.5 m/s',
                            marker: {color: 'rgb(92,131,47)'},
                            type: 'area'
                        };

                        var trace12 = {
                            r: data[0].trace12,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '5.5-6 m/s',
                            marker: {color: 'rgb(56,37,19)'},
                            type: 'area'
                        };

                        var trace13 = {
                            r: data[0].trace13,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '> 6 m/s',
                            marker: {color: 'rgb(99,166,159)'},
                            type: 'area'
                        };

                        var data_rose = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13];

                        var layout = {
                            title: 'GRAFIK WIND ROSE',
                            font: {size: 16},
                            legend: {font: {size: 16}},
                            radialaxis: {ticksuffix: '%'},
                            orientation: 270
                        };

                        $("div#loader").removeClass('active');
                        Plotly.newPlot(graph1, data_rose, layout);
                    });
                }
            });
        },
        onClear: function(){
            $("div#tanggal_akhir").empty();
            $("div#WRS").empty();
        }
    });
});