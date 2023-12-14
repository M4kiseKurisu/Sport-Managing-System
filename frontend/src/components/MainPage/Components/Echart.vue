<template>
    <div style="width: 360px; height: 460px; margin-top: 30px;" id="main1"></div>
</template>
  
<script>
import * as echarts from 'echarts';
import axios from 'axios';
export default {
    name: "echarts",
    data() {
        return {
            dataList: [],
        }
    },
    mounted() {
        this.dataList = this.inputList;
        console.log(this.dataList);
        this.fetchUserInfoAndActivity()
    },
    methods: {
        async fetchUserInfoAndActivity() {
            try {
                const activityResponse = await axios.get("http://127.0.0.1:8000/api/user/activity/statistic", {
                    params: {
                        uid: JSON.parse(sessionStorage.getItem("uid")),
                    },
                });

                console.log(activityResponse);

                if (activityResponse.data.status) {
                    this.dataList = [];
                    this.dataList.push({ name: "篮球", value: activityResponse.data.data["篮球"] });
                    this.dataList.push({ name: "足球", value: activityResponse.data.data["足球"] });
                    this.dataList.push({ name: "跑步", value: activityResponse.data.data["跑步"] });
                    this.dataList.push({ name: "健身", value: activityResponse.data.data["健身"] });
                    this.dataList.push({ name: "飞盘", value: activityResponse.data.data["飞盘"] });
                    this.dataList.push({ name: "羽毛球", value: activityResponse.data.data["羽毛球"] });
                    this.dataList.push({ name: "桌球", value: activityResponse.data.data["桌球"] });
                    this.dataList.push({ name: "排球", value: activityResponse.data.data["排球"] });
                    this.dataList.push({ name: "乒乓球", value: activityResponse.data.data["乒乓球"] });
                    this.dataList.push({ name: "游泳", value: activityResponse.data.data["游泳"] });
                    this.dataList.push({ name: "其他", value: activityResponse.data.data["其他"] });

                    if (!activityResponse.data.data["篮球"]
                        && !activityResponse.data.data["足球"]
                        && !activityResponse.data.data["跑步"]
                        && !activityResponse.data.data["健身"]
                        && !activityResponse.data.data["飞盘"]
                        && !activityResponse.data.data["羽毛球"]
                        && !activityResponse.data.data["桌球"]
                        && !activityResponse.data.data["排球"]
                        && !activityResponse.data.data["乒乓球"]
                        && !activityResponse.data.data["游泳"]
                        && !activityResponse.data.data["其他"]) {
                        this.dataList.push({ name: "暂无活动", value: 0 });
                    }
                }

                console.log(this.dataList);
            } catch (error) {
                console.error(error);
            }
            this.echartsInit()
        },
        echartsInit() {
            echarts.init(document.getElementById('main1')).setOption({
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '0%',
                    left: 'center'
                },
                series: [
                    {
                        name: '活动类型统计',
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
                        data: this.dataList,
                    }
                ]
            })
        }

    }
}
</script>
  
<style scoped></style>