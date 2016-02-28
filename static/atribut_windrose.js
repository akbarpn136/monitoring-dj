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

            $("div#WRS").empty();
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

                    $("div#WRS").empty();
                    selector_tgl_akr.attr("data-value", b);

                    $("div#loader").addClass('active');

                    $.get('/monitor/' + daerah_tertentu1 + '/rose/' + $("span#data_tgl_awl").attr("data-value") + '/' + selector_tgl_akr.attr("data-value"), function(data){
                        var trace1 = {
                            r: data[0].trace1,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '0.0-0.5 m/s', // purple
                            marker: {color: '#a333c8'},
                            type: 'area'
                        };

                        var trace2 = {
                            r: data[0].trace2,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '0.5-1.0 m/s',
                            marker: {color: 'a5673f'}, // brown
                            type: 'area'
                        };

                        var trace3 = {
                            r: data[0].trace3,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '1.0-1.5 m/s',
                            marker: {color: '#21ba45'}, // green
                            type: 'area'
                        };

                        var trace4 = {
                            r: data[0].trace4,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '1.5-2.0 m/s',
                            marker: {color: '#6435c9'}, // violet
                            type: 'area'
                        };

                        var trace5 = {
                            r: data[0].trace5,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '2.0-2.5 m/s',
                            marker: {color: '#fbbd08'}, // yellow
                            type: 'area'
                        };

                        var trace6 = {
                            r: data[0].trace6,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '2.5-3.0 m/s',
                            marker: {color: '#2185d0'}, // blue
                            type: 'area'
                        };

                        var trace7 = {
                            r: data[0].trace7,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '3.0-3.5 m/s',
                            marker: {color: '#b5cc18'}, // olive
                            type: 'area'
                        };

                        var trace8 = {
                            r: data[0].trace8,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '3.5-4.0 m/s',
                            marker: {color: '#767676'}, // grey
                            type: 'area'
                        };

                        var trace9 = {
                            r: data[0].trace9,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '4.0-4.5 m/s',
                            marker: {color: '#00b5ad'}, // teal
                            type: 'area'
                        };

                        var trace10 = {
                            r: data[0].trace10,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '4.5-5.0 m/s',
                            marker: {color: '#f2711c'}, // orange
                            type: 'area'
                        };

                        var trace11 = {
                            r: data[0].trace11,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '5.0-5.5 m/s',
                            marker: {color: '#1b1c1d'}, // black
                            type: 'area'
                        };

                        var trace12 = {
                            r: data[0].trace12,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '5.5-6.0 m/s',
                            marker: {color: '#e03997'}, // pink
                            type: 'area'
                        };

                        var trace13 = {
                            r: data[0].trace13,
                            t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                            name: '> 6 m/s',
                            marker: {color: '#db2828'}, // red
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