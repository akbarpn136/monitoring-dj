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

            $("div#PDF").empty();
            $("span#data_tgl_awl").attr("data-value", a);
            $("div#tanggal_akhir").append().html(inpt);
            $("input#in_tgl_akhir").Zebra_DatePicker({
                show_icon: false,
                onClear: function(){
                    $("div#jenis_grafik").empty();
                    $("div#PDF").empty();
                },
                onSelect: function(b){
                    var selector_tgl_akr = $("span#data_tgl_akr");
                    var daerah_tertentu1 = $("span#data_daerah").attr("data-value");
                    var graph1=document.getElementById("PDF");

                    $("div#PDF").empty();
                    selector_tgl_akr.attr("data-value", b);

                    $("div#loader").addClass('active');

                    $.get('/monitor/' + daerah_tertentu1 + '/pdf/' + $("span#data_tgl_awl").attr("data-value") + '/' + selector_tgl_akr.attr("data-value"), function(data){
                        var trace1 = {
                            x: data[0].velo,
                            name: 'Probabilitas Kecepatan Angin',
                            marker: {color: '#00b5ad'}, // teal
                            type: 'histogram'
                        };

                        var trace2 = {
                            x: data[0].velo,
                            y: data[0].veloy,
                            type: 'scatter'
                        };

                        console.log(data[0]);

                        var data_pdf = [trace2];

                        var layout = {
                            title: 'GRAFIK DISTRIBUSI KECEPATAN ANGIN',
                            font: {size: 16},
                            legend: {font: {size: 16}},
                            xaxis: {
                                title: 'Kecepatan Angin (m/s)'
                            }
                        };

                        $("div#loader").removeClass('active');
                        Plotly.newPlot(graph1, data_pdf, layout, {showLink: false, displaylogo: false, scrollZoom: true});
                    });
                }
            });
        },
        onClear: function(){
            $("div#tanggal_akhir").empty();
            $("div#PDF").empty();
        }
    });
});