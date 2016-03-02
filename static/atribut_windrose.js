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
                    $("div#v_step").empty();
                    selector_tgl_akr.attr("data-value", b);

                    var inpt_v_max = '<input id="inpt_vmax" type="text" placeholder="V max">';
                    var inpt_v_step = '<input id="inpt_vstep" type="text" placeholder="V step">';

                    $("div#v_max").append().html(inpt_v_max);
                    $("input#inpt_vmax").change(function(){
                        var nilai_inpt_vmax = $(this).val();

                        $("div#v_step").append().html(inpt_v_step);
                        $("input#inpt_vstep").change(function(){
                            $("div#WRS").empty();
                            var nilai_inpt_vstep = $(this).val();

                            $("div#loader").addClass('active');

                            $.get('/monitor/' + daerah_tertentu1 + '/rose/' + $("span#data_tgl_awl").attr("data-value") + '/' + selector_tgl_akr.attr("data-value") + '/' + nilai_inpt_vmax + '/' + nilai_inpt_vstep, function(data){
                                var dt_rose = [];
                                $.each(data, function(k, v){
                                    var tr = {
                                        r: v.slice(0, 8),
                                        t: ['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
                                        name: v.slice(8,9),
                                        marker: {color: '#'+ v.slice(9)}, // purple
                                        type: 'area'
                                    };

                                    dt_rose.push(tr);
                                });

                                var layout = {
                                    title: 'GRAFIK WIND ROSE',
                                    font: {size: 16},
                                    legend: {font: {size: 16}},
                                    radialaxis: {ticksuffix: '%'},
                                    orientation: 270
                                };

                                $("div#loader").removeClass('active');
                                Plotly.newPlot(graph1, dt_rose, layout);
                            });
                        });
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