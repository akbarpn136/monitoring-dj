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

            $("div#ATR").empty();
            $("span#data_tgl_awl").attr("data-value", a);
            $("div#tanggal_akhir").append().html(inpt);
            $("input#in_tgl_akhir").Zebra_DatePicker({
                show_icon: false,
                onClear: function(){
                    $("div#jenis_grafik").empty();
                    $("div#ATR").empty();
                },
                onSelect: function(b){
                    var slct = '<select id="selek" class="ui search dropdown">';
                    slct += '<option value="0">Jenis grafik</option>';
                    slct += '<option value="1">Kecepatan Angin</option>';
                    slct += '<option value="2">Arah Angin</option>';
                    slct += '<option value="3">Data Getaran</option>';
                    slct += '</select>';

                    $("div#ATR").empty();
                    $("span#data_tgl_akr").attr("data-value", b);
                    $("div#jenis_grafik").append().html(slct);
                    $("select#selek").dropdown({
                        placeholder: false,
                        onChange: function(nilai_pilihan){
                            if(nilai_pilihan == 1)
                            {
                                $("div#ATR").empty();
                                var graph1=document.getElementById("ATR");
                                var key_x1 = [];
                                var key_y1 = [];
                                var ttl_x1 = $("span#data_title_x");
                                var ttl_y1 = $("span#data_title_y");
                                var jdl_bsr1 = $("span#data_judul_besar");

                                ttl_x1.attr("data-value", "Waktu");
                                ttl_y1.attr("data-value", "Kecepatan Angin (m/s)");
                                jdl_bsr1.attr("data-value", "GRAFIK KECEPATAN ANGIN");

                                var daerah_tertentu1 = $("span#data_daerah").attr("data-value");
                                var title_x1 = ttl_x1.attr("data-value");
                                var title_y1 = ttl_y1.attr("data-value");
                                var judul_besar1 = jdl_bsr1.attr("data-value");

                                var trace11 = [{
                                    x: key_x1,
                                    y: key_y1,
                                    type: 'scatter'
                                }];

                                var layout1 = {
                                    title: judul_besar1,
                                    showlegend: false,
                                    xaxis: {
                                        title: title_x1
                                    },
                                    yaxis: {
                                        title: title_y1
                                    }
                                };

                                $("div#loader").addClass('active');

                                $.get('/monitor/' + daerah_tertentu1 + '/atribut/' + $("span#data_tgl_awl").attr("data-value") + '/' + $("span#data_tgl_akr").attr("data-value"), function(data){
                                    $.each(data, function(a, b){
                                        key_x1.push(b.fields.tanggal+' '+b.fields.waktu);
                                        key_y1.push(b.fields.kecepatan);
                                    });

                                    $("div#loader").removeClass('active');
                                    Plotly.newPlot(graph1, trace11, layout1, {showLink: false, displaylogo: false, scrollZoom: true});
                                });
                            }

                            else if(nilai_pilihan == 2)
                            {
                                $("div#ATR").empty();
                                var graph2=document.getElementById("ATR");
                                var key_x2 = [];
                                var key_y2 = [];
                                var ttl_x2 = $("span#data_title_x");
                                var ttl_y2 = $("span#data_title_y");
                                var jdl_bsr2 = $("span#data_judul_besar");

                                ttl_x2.attr("data-value", "Waktu");
                                ttl_y2.attr("data-value", "Arah Angin (derajat)");
                                jdl_bsr2.attr("data-value", "GRAFIK ARAH ANGIN");

                                var daerah_tertentu2 = $("span#data_daerah").attr("data-value");
                                var title_x2 = ttl_x2.attr("data-value");
                                var title_y2 = ttl_y2.attr("data-value");
                                var judul_besar2 = jdl_bsr2.attr("data-value");

                                var trace12 = [{
                                    x: key_x2,
                                    y: key_y2,
                                    type: 'scatter'
                                }];

                                var layout2 = {
                                    title: judul_besar2,
                                    showlegend: false,
                                    xaxis: {
                                        title: title_x2
                                    },
                                    yaxis: {
                                        title: title_y2
                                    }
                                };

                                $("div#loader").addClass('active');

                                $.get('/monitor/'+ daerah_tertentu2 + '/atribut/' + $("span#data_tgl_awl").attr("data-value") + '/' + $("span#data_tgl_akr").attr("data-value"), function(data){
                                    $.each(data, function(a, b){
                                        key_x2.push(b.fields.tanggal+' '+b.fields.waktu);
                                        key_y2.push(b.fields.arah);
                                    });

                                    $("div#loader").removeClass('active');
                                    Plotly.newPlot(graph2, trace12, layout2, {showLink: false, displaylogo: false, scrollZoom: true});
                                });
                            }

                            else if(nilai_pilihan == 3)
                            {
                                $("div#ATR").empty();
                                var graph3=document.getElementById("ATR");
                                var key_x3 = [];
                                var key_y3 = [];
                                var ttl_x3 = $("span#data_title_x");
                                var ttl_y3 = $("span#data_title_y");
                                var jdl_bsr3 = $("span#data_judul_besar");

                                ttl_x3.attr("data-value", "Waktu");
                                ttl_y3.attr("data-value", "Getaran (m/s2)");
                                jdl_bsr3.attr("data-value", "GRAFIK GETARAN AKIBAT ANGIN");

                                var daerah_tertentu3 = $("span#data_daerah").attr("data-value");
                                var title_x3 = ttl_x3.attr("data-value");
                                var title_y3 = ttl_y3.attr("data-value");
                                var judul_besar3 = jdl_bsr3.attr("data-value");

                                var trace13 = [{
                                    x: key_x3,
                                    y: key_y3,
                                    type: 'scatter'
                                }];

                                var layout3 = {
                                    title: judul_besar3,
                                    showlegend: false,
                                    xaxis: {
                                        title: title_x3
                                    },
                                    yaxis: {
                                        title: title_y3
                                    }
                                };

                                $("div#loader").addClass('active');

                                $.get('/monitor/'+ daerah_tertentu3 + '/atribut/' + $("span#data_tgl_awl").attr("data-value") + '/' + $("span#data_tgl_akr").attr("data-value"), function(data){
                                    $.each(data, function(a, b){
                                        key_x3.push(b.fields.tanggal+' '+b.fields.waktu);
                                        key_y3.push(b.fields.akselerator5);
                                    });

                                    $("div#loader").removeClass('active');
                                    Plotly.newPlot(graph3, trace13, layout3, {showLink: false, displaylogo: false, scrollZoom: true});
                                });
                            }

                            else
                            {
                                $("div#ATR").empty();
                            }
                        }
                    });
                }
            });
        },
        onClear: function(){
            $("div#tanggal_akhir").empty();
            $("div#ATR").empty();
        }
    });
});