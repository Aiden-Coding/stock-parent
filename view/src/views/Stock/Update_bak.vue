<template>
  <ChartLayout title="实时更新">
    <div id="update-k-line" class="k-line-chart"></div>
  </ChartLayout>
</template>

<script>
import { dispose, init } from 'klinecharts'
import generatedDataList from './generatedDataList'
// 引入js
import { KLineChartPro, DefaultDatafeed } from 'npm_klinecharts_pro'
// 引入样式
import 'npm_klinecharts_pro/dist/klinecharts-pro.css'
import initData from './initData'
import ChartLayout from './ChartLayout.vue'

export default {
  name: 'ChartUpdate',
  components: { ChartLayout },
  data: function () {
    return {
      dataList: []
    }
  },
  mounted: function () {
    // 创建实例
    const chart = new KLineChartPro({
      container: document.getElementById('container'),
      // 初始化标的信息
      symbol: {
        exchange: 'XNYS',
        market: 'stocks',
        name: 'Alibaba Group Holding Limited American Depositary Shares, each represents eight Ordinary Shares',
        shortName: 'BABA',
        ticker: 'BABA',
        priceCurrency: 'usd',
        type: 'ADRC'
      },
      // 初始化周期
      period: { multiplier: 15, timespan: 'minute', text: '15m' },
      // 这里使用默认的数据接入，如果实际使用中也使用默认数据，需要去 https://polygon.io/ 申请 API key
      datafeed: new DefaultDatafeed(`${polygonIoApiKey}`)
    })
  },
  unmounted: function () {
    dispose('update-k-line')
  }
}
</script>
<style>
.k-line-chart-container {
  display: flex;
  flex-direction: column;
  margin: 15px;
  border-radius: 2px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  background-color: #ffffff;
  width: 620px;
  height: 440px;
  padding: 16px 6px 16px 16px;
}

.k-line-chart-title {
  margin: 0;
  color: #252525;
  padding-bottom: 10px;
}

.k-line-chart {
  display: flex;
  flex: 1;
}
.k-line-chart-menu-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 10px;
  font-size: 12px;
  color: #606060;
}
.k-line-chart-menu-container button {
  cursor: pointer;
  background-color: #1677ff;
  border-radius: 2px;
  margin-right: 8px;
  height: 24px;
  line-height: 26px;
  padding: 0 6px;
  font-size: 12px;
  color: #fff;
  border: none;
  outline: none;
}
</style>
