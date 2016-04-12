/**
 * Created by syariefa on 2/27/16.
 */
$(document).ready(function(){
    var link_rms = '/monitor/rms/';
    $("input#vmax").change(function(){
        var vmax_val = $(this).val();
        if(vmax_val == '' || vmax_val == 0)
        {
            $("div#tanggal_akhir").empty();
            $("div#rms").empty();
        }

        else
        {
            $("div#rms").empty();
            var input_grup = '<input id="grup_v" type="text" placeholder="Jumlah kelompok kecepatan">';
            $("div#tanggal_akhir").append().html(input_grup);

             $("input#grup_v").change(function(){
                 var grup_v_val = $(this).val();

                 $("div#loader").addClass('active');

                 $.get(link_rms+vmax_val+'/'+grup_v_val, function(nilai_rms_json){
                     var graph1=document.getElementById("RMS");
                     var trace1 = {
                         x: nilai_rms_json['data_x'],
                         y: nilai_rms_json['data_y'],
                         fill: 'tozeroy',
                         type: 'scatter',
                         showlegend: false
                     };
                     var layout1 = {
                         title: 'Grafik RMS Getaran',
                         xaxis: {
                             title: "Kelompok Kecepatan (m/s)"
                         },
                         yaxis: {
                             title: "RMS Getaran"
                         }
                     };

                     var data = [trace1];
                     $("div#loader").removeClass('active');
                     Plotly.newPlot(graph1, data, layout1, {showLink: false, displaylogo: false, scrollZoom: true});
                     Plotly.redraw(graph1);
                 });
             });
        }
    });
});