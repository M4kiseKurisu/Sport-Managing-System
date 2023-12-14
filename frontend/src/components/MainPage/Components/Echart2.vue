<template>
    <div style="width: 360px; height: 460px; margin-top: 30px;" id="main2"></div>
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
                const activityResponse = await axios.get("http://127.0.0.1:8000/api/user/group/statistic", {
                    params: {
                        uid: JSON.parse(sessionStorage.getItem("uid")),
                    },
                });

                console.log(activityResponse);

                if (activityResponse.data.status) {
                    this.dataList = [];
                    this.dataList.push({ name: "娱乐", value: activityResponse.data.data["娱乐"] });
                    this.dataList.push({ name: "竞技", value: activityResponse.data.data["竞技"] });
                    this.dataList.push({ name: "综合", value: activityResponse.data.data["综合"] });
                    this.dataList.push({ name: "户外", value: activityResponse.data.data["户外"] });
                    this.dataList.push({ name: "社交", value: activityResponse.data.data["社交"] });
                    this.dataList.push({ name: "健身", value: activityResponse.data.data["健身"] });
                    this.dataList.push({ name: "摸鱼", value: activityResponse.data.data["摸鱼"] });

                    if (!activityResponse.data.data["娱乐"]
                        && !activityResponse.data.data["竞技"]
                        && !activityResponse.data.data["综合"]
                        && !activityResponse.data.data["户外"]
                        && !activityResponse.data.data["社交"]
                        && !activityResponse.data.data["健身"]
                        && !activityResponse.data.data["摸鱼"]) {
                        this.dataList.push({ name: "暂无团体", value: 0 });
                    }
                }

                console.log(this.dataList);
            } catch (error) {
                console.error(error);
            }
            this.echartsInit()
        },
        echartsInit() {
            echarts.init(document.getElementById('main2')).setOption({
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