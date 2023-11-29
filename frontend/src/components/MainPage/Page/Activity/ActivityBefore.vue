<template>
    <!-- 界面标题 -->
    <div class="title">
        <div>过往活动</div>
    </div>

    <!-- 表项 -->
    <div>
        <BeforeActivityRow :information="list[0]" />
    </div>
</template>

<script>
import axios from 'axios'
import BeforeActivityRow from '../../Components/BeforeActivityRow.vue';
export default {
    data() {
        return {
            list: [
                {
                    "aid": 1111,
                    "name": "1111",
                    "type": "个人",
                    "category": "篮球",
                    "capacity": 1,
                    "maximum": 500,
                    "start_time": "2023-10-30 15:00:00",
                    "end_time": "2023-10-30 18:00:00",
                    "picture": "/media/images/activity/20231127190029_59.jpg",
                    "favor": 0,
                    "is_joined": false
                }
            ],
        };
    },
    methods: {
        draw() {
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/activity/view/inactive",
                params: {
                    uid: JSON.parse(sessionStorage.getItem("uid")),
                    type: 2,
                    method: "time"
                }
            }).then((result) => {
                if (result.data.status) {
                    this.list = result.data.list;
                }
            });
        }
    },
    created() {
        this.draw()
    },
    components: { BeforeActivityRow }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.row {
    width: 60%;
    height: 200px;
}
</style>