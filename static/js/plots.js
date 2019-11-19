//word cloud

var chartVars = "KoolOnLoadCallFunction=chartReadyHandler";

KoolChart.create("chart1", "chartHolder", chartVars, "100%", "100%");

function chartReadyHandler(id) {
  document.getElementById(id).setLayout(layoutStr);
  document.getElementById(id).setData(makeData());
  //setTimeout(changeData, 30000);
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
  var i, n,
  chartData = [];
  var data1 = ["apple","orange","cow", "moon"]
  var data4 = [{text: "Jen", weight: 60}, {text:"william",weight:30}]
  var data5 = [{text: "relative", weight: 60}, {text:"weights",weight:30}, {text:"maybe",weight:1}]
  
  for(i = 0, n = data1.length ; i < n ; i += 1){
   chartData.push({
    text : data1[i],
    weight : Math.floor(Math.random(10) * 100)
   });
  }
  chartData=chartdata;

  console.log(chartData);
  return chartData;
 };
