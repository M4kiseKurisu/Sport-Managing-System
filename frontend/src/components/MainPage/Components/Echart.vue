<template>
    <div style="width: 400px; height: 400px" id="main"></div>
</template>
  
<script>
import * as echarts from 'echarts';
export default {
    name: "echarts",
    data() {
        return {}
    },
    mounted() {
        this.echartsInit()
    },
    methods: {
        echartsInit() {
            echarts.init(document.getElementById('main')).setOption({
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 32,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: 2, name: '活动A' },
                            { value: 6, name: '活动B' },
                            { value: 5, name: '活动C' },
                            { value: 4, name: '活动D' },
                            { value: 8, name: '活动E' }
                        ]
                    }
                ]
            })
        }

    }
}
</script>
  
<style scoped></style>