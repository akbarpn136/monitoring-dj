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

            $("div#WTR").empty();
            $("span#data_tgl_awl").attr("data-value", a);
            $("div#tanggal_akhir").append().html(inpt);
            $("input#in_tgl_akhir").Zebra_DatePicker({
                show_icon: false,
                onClear: function(){
                    $("div#jenis_grafik").empty();
                    $("div#WTR").empty();
                },
                onSelect: function(b){
                    var selector_tgl_akr = $("span#data_tgl_akr");
                    var daerah_tertentu1 = $("span#data_daerah").attr("data-value");
                    var graph1=document.getElementById("WTR");

                    $("div#WTR").empty();
                    $("div#v_step").empty();
                    selector_tgl_akr.attr("data-value", b);

                    var inpt_v_max = '<input id="inpt_vmax" type="text" placeholder="V max">';
                    var inpt_v_step = '<input id="inpt_vstep" type="text" placeholder="V step">';

                    $("div#v_max").append().html(inpt_v_max);
                    $("input#inpt_vmax").change(function(){
                        var nilai_inpt_vmax = $(this).val();

                        $("div#v_step").append().html(inpt_v_step);
                        $("input#inpt_vstep").change(function(){
                            $("div#WTR").empty();
                            var nilai_inpt_vstep = $(this).val();
                            var selektor_kompas = '<select id="slk_kmps" class="ui dropdown">';
                            selektor_kompas += '<option value="">Arah angin</option>';
                            selektor_kompas += '<option value="UT">Utara</option>';
                            selektor_kompas += '<option value="TL">Timur Laut</option>';
                            selektor_kompas += '<option value="TM">Timur</option>';
                            selektor_kompas += '<option value="TG">Tenggara</option>';
                            selektor_kompas += '<option value="SL">Selatan</option>';
                            selektor_kompas += '<option value="BD">Barat Daya</option>';
                            selektor_kompas += '<option value="BR">Barat</option>';
                            selektor_kompas += '<option value="BL">Barat Laut</option>';
                            selektor_kompas += '</select>';

                            $("div#kompas").append().html(selektor_kompas);
                            $("select#slk_kmps").dropdown({
                                placeholder: false,
                                onChange: function(dt_kmps){
                                    $("div#WTR").empty();
                                    $("div#loader").addClass('active');
                                    $.get('/monitor/' + daerah_tertentu1 + '/wtr/' + $("span#data_tgl_awl").attr("data-value") + '/' + selector_tgl_akr.attr("data-value") + '/' + nilai_inpt_vmax + '/' + nilai_inpt_vstep + '/' + dt_kmps, function(data){
                                        var dt_wtr = [];
                                        $.each(data, function(ky, v){
                                            var tr = {
                                                x: v[3],
                                                y: v[2],
                                                z: v[4],
                                                mode: 'lines',
                                                name: v[0],
                                                marker: {
                                                    color: v[1],
                                                    size: 9,
                                                    symbol: 'circle',
                                                    line: {
                                                      color: 'rgb(0,0,0)',
                                                      width: 2
                                                    }
                                                },
                                                line: {
                                                    color: v[1],
                                                    width: 1
                                                },
                                                type: 'scatter3d'
                                            };

                                            dt_wtr.push(tr);
                                        });

                                        var layout = {
                                            title: 'GRAFIK Water Fall',
                                            font: {size: 16},
                                            margin: {
                                                l: 0,
                                                r: 0,
                                                b: 0,
                                                t: 65
                                            },
                                            xaxis: {
                                                title: 'Grup kecepatan'
                                            },
                                            yaxis: {
                                                title: 'Frekuensi'
                                            },
                                            zaxis: {
                                                title: 'Amplitudo'
                                            }
                                        };

                                        $("div#loader").removeClass('active');
                                        Plotly.newPlot(graph1, dt_wtr, layout);
                                    });
                                }
                            });
                        });
                    });

                }
            });
        },
        onClear: function(){
            $("div#tanggal_akhir").empty();
            $("div#WTR").empty();
        }
    });
});