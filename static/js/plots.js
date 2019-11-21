//word cloud

var chartVars = "KoolOnLoadCallFunction=chartReadyHandler";

KoolChart.create("chart1", "chartHolder", chartVars, "100%", "100%");

function chartReadyHandler(id) {
  document.getElementById(id).setLayout(layoutStr);
  document.getElementById(id).setData(makeData());
}

var layoutStr =
  '<KoolChart backgroundColor="#007bff"  borderStyle="none" fontFamily="Noto Sans">'
   +'<Options>'
    +'<Caption color="#FFFFFF" text="These are the words that matched to the category. The bigger size means they contributed more to the prediction"/>'
   +'</Options>'
   +'<WordCloudChart showDataTips="true">'
    +'<series>'
     +'<WordCloudSeries textField="text" weightField="weight">'
      +'<showDataEffect>'
       +'<SeriesInterpolate duration="3000"/>'
      +'</showDataEffect>'
      +'<fills>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
       +'<SolidColor color="#FFFFFF"/>'
      +'</fills>'
     +'</WordCloudSeries>'
    +'</series>'
   +'</WordCloudChart>'
  +'</KoolChart>';

function changeData(){
  document.getElementById("chart1").setData(makeData());
  setTimeout(changeData, 500);
 }

 function makeData(){
  chartData = [];
  chartData=chartdata;
  return chartData;
 };
