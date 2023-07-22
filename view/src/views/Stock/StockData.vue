<template>
  <!-- <button @click="hel()">hello</button> -->
  <div :class="prefixCls">
    <div id="container" class="k-line-chart"></div>
  </div>
</template>

<script setup>
import { dispose, init, CandleType } from 'klinecharts'
import { onUnmounted, onMounted, reactive, watch } from 'vue'
import generatedDataList from './generatedDataList'
// 引入js
import { KLineChartPro } from 'npm_klinecharts_pro'
// 引入js
import CustDefaultDatafeed from './CustDefaultDatafeed'
// 引入样式
import 'npm_klinecharts_pro/dist/klinecharts-pro.css'
import initData from './initData'
import { useDesign } from '@/hooks/web/useDesign'
import { getIdApi, addApi, getPicTagApi, deleteByIdPicTagApi } from '@/api/stockPicTag'
const { getPrefixCls } = useDesign()
const prefixCls = getPrefixCls('update')
let chartViewData = reactive({
  chart: '',
  ticker: ''
})
// 初始化所有主题色
onMounted(() => {
  // 创建实例
  let chart = new KLineChartPro({
    container: document.getElementById('container'),
    watermark: '',
    styles: {
      candle: {
        // 蜡烛柱
        bar: {
          upColor: '#FF0000',
          downColor: '#40E0D0',
          noChangeColor: '#888888',
          upBorderColor: '#FF0000',
          downBorderColor: '#40E0D0',
          noChangeBorderColor: '#888888',
          upWickColor: '#FF0000',
          downWickColor: '#40E0D0',
          noChangeWickColor: '#888888'
        }
      }
    },
    // 初始化标的信息
    symbol: {
      // exchange: 'XNYS',
      // market: 'stocks',
      name: '平安银行',
      shortName: '平安银行(000001)',
      ticker: '000001',
      priceCurrency: 'cny',
      type: 'ADRC'
    },
    periods: [
      // { multiplier: 1, timespan: 'second', text: '分时', candleType: CandleType.Area },
      { multiplier: 1, timespan: 'day', text: '日K', candleType: CandleType.CandleSolid },
      { multiplier: 1, timespan: 'week', text: '周K', candleType: CandleType.CandleSolid },
      { multiplier: 1, timespan: 'month', text: '月K', candleType: CandleType.CandleSolid }
    ],
    // 初始化周期
    period: {
      multiplier: 1,
      timespan: 'day',
      text: '日K',
      candleType: CandleType.CandleSolid
    },
    drawingBarVisible: false,
    datafeed: new CustDefaultDatafeed(),
    onDrawEnd: (event) => {
      console.log('End')
      console.log(event)
      let data = {
        id: event.overlay.id,
        name: event.overlay.extendData.symbol.name,
        code: event.overlay.extendData.symbol.ticker,
        timespan: event.overlay.extendData.period.timespan,
        tagClass: event.overlay.name
      }
      const pointsT = []
      for (const item of event.overlay.points) {
        pointsT.push({ timestamp: item.timestamp, value: item.value })
      }
      data.tagText = JSON.stringify(pointsT)
      //save
      addApi(data)
        .then((response) => {
          console.log(response.data)
        })
        .catch((error) => {
          console.log('An error occurred:', error)
        })
    },
    onDrawStart: async (event) => {
      console.log('res')
      const res = await getIdApi()
      console.log(res)
      event.overlay.id = res.data
    },
    onSymbolOrPeriodChange: () => {
      initPicTag(chartViewData.chart.getSymbol().ticker, chartViewData.chart.getPeriod().timespan)
    },
    onRemoveOverlayById: (value) => {
      deleteByIdPicTagApi(value)
    }
  })
  // chart.setTheme('dark')

  // chart.getChart().createOverlay({
  //   id: '23',
  //   name: 'rayLine',
  //   extendData: 'Override overlay',
  //   // points: [
  //   //   { timestamp: 1678118400000, value: 13.527306451612905 },
  //   //   { timestamp: 1681920000000, value: 12.2705 }
  //   // ],
  //   lock: true,
  //   styles: { text: { color: 'rgba(100, 10, 200, .3)' } },
  //   onDrawEnd: function ({ overlay }) {
  //     // Listen to the completion of drawing and overwrite the attribute
  //     console.log(overlay)
  //   }
  // })
  // console.log(chart.getChart().getOverlayById('23'))
  // chart.getChart().setOffsetRightDistance(0)
  // chart.getChart().setLeftMinVisibleBarCount(155)

  // chart.getChart().setRightMinVisibleBarCount(20)
  initPicTag(chart.getSymbol().ticker, chart.getPeriod().timespan)
  chartViewData.chart = chart
  chartViewData.ticker = chartViewData.chart.getSymbol().ticker
})
const initPicTag = (ticker, timespan) => {
  getPicTagApi(ticker, timespan).then((result) => {
    let a = []
    for (let i = 0; i < result.data.length; i++) {
      a.push(result.data[i].id)
      console.log(result.data[i].tagText)
      chartViewData.chart.createOverlay({
        id: result.data[i].id,
        name: result.data[i].tagClass,
        lock: true,
        points: JSON.parse(result.data[i].tagText)
      })
    }
    chartViewData.chart.setOverlayIds(a)
  })
}
const hel = () => {
  chartViewData.ticker = '000815'
  chartViewData.chart.setSymbol({
    exchange: 'XNYS',
    market: 'stocks',
    name: 'Alibaba Group Holding Limited American Depositary Shares, each represents eight Ordinary Shares',
    shortName: '美利云',
    ticker: '000815',
    priceCurrency: 'usd',
    type: 'ADRC'
  })
}
// 控制台自动打印：obj.a从1改变为2
onUnmounted(() => {
  dispose('container')
})
</script>
<style lang="less" scoped>
@prefix-cls: ~'@{namespace}-update';

.@{prefix-cls} {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  .k-line-chart {
    position: absolute;
    height: 100%;
    top: 0;
    left: 0;
    width: 100%;
  }
}

// .k-line-chart-container {
//   /* display: flex;
//   flex-direction: column; */
//   /* margin: 15px; */
//   /* border-radius: 2px; */
//   /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3); */
//   background-color: #ffffff;
//   height: 100%;
//   /* padding: 16px 6px 16px 16px; */
// }
</style>
