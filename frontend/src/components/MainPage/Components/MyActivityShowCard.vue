<template>
    <div class="border">
        <div class="header">
            <div class="topic">{{ name }}</div>


            <div class="like-button">
                <div class="heart-icon" :class="{ 'liked': liked }" @click="toggleLike">
                    <i class="fas fa-heart"></i>
                </div>
                <div class="like-count">{{ likeCount }}</div>
            </div>
        </div>

        <div class="text">开始时间：{{ start_time }}</div>
        <div class="text">结束时间：{{ end_time }}</div>
        <div class="text">活动类型：{{ category }}</div>
        <div class="text">活动人数/容量：{{ capacity }} / {{ maximum }}</div>
        <div class="buttonContainer">
            <div class="button">
                <el-button type="primary" @click="checkInformation()">查看详情</el-button>
                <el-button type="danger" @click="getOut()">退出/撤销活动</el-button>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import dayjs from 'dayjs'
export default {
    data() {
        return {
            liked: this.is_favor,
            likeCount: this.favor
        }
    },
    methods: {
        toggleLike() {
            if (this.end_time > dayjs().format('YYYY-MM-DD HH:mm:ss')) {
                this.$message({
                    showClose: true,
                    message: "不能在活动结束前点赞！",
                    type: 'error'
                });
                return;
            }

            if (this.liked) {
                let information = {
                    uid: JSON.parse(sessionStorage.getItem('uid')),
                    aid: this.aid,
                    method: "remove"
                }

                axios({
                    method: "POST",
                    url: "http://127.0.0.1:8000/api/activity/favor",
                    data: information
                }).then((result) => {
                    if (result.data.status) {
                        this.$message({
                            showClose: true,
                            message: result.data.msg,
                            type: 'success'
                        });
                    }
                });

                this.liked = !this.liked;
                this.likeCount--;
            }

            else {
                let information = {
                    uid: JSON.parse(sessionStorage.getItem('uid')),
                    aid: this.aid,
                    method: "like"
                }

                axios({
                    method: "POST",
                    url: "http://127.0.0.1:8000/api/activity/favor",
                    data: information
                }).then((result) => {
                    if (result.data.status) {
                        this.$message({
                            showClose: true,
                            message: result.data.msg,
                            type: 'success'
                        });
                    }
                });

                this.liked = !this.liked;
                this.likeCount++;
            }
        },
        checkInformation() {
            this.$router.push('/Page/Activity_Information/Detail/' + this.aid);
        },
        getOut() {
            if (this.start_time < dayjs().format('YYYY-MM-DD HH:mm:ss')) {
                this.$message({
                    showClose: true,
                    message: "不能退出已经开始的活动！",
                    type: 'error'
                });
                return;
            }

            let information = {
                uid: JSON.parse(sessionStorage.getItem('uid')),
                aid: this.aid
            }

            axios({
                method: "POST",
                url: "http://127.0.0.1:8000/api/activity/exit",
                data: information
            }).then((result) => {
                if (result.data.status) {
                    this.$message({
                        showClose: true,
                        message: result.data.msg,
                        type: 'success'
                    });
                }
            });
        }
    },
    props: ["name", "start_time", "end_time", "category",
        "capacity", "maximum", "favor", "is_favor", "aid"]
}
</script>

<style scoped>
.header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 15px;
}

.border {
    border: 4px solid #4c82ff63;
    border-radius: 8px;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 15px;
    padding-right: 15px;
}

.topic {
    font-size: 20px;
}

.text {
    font-size: 16px;
    margin-top: 10px;
}

.buttonContainer {
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.like-button {
    display: flex;
    align-items: center;
    height: 24px;
}

.heart-icon {
    cursor: pointer;
    width: 24px;
    height: 24px;
    margin-right: 8px;
    position: relative;
}

.heart-icon i {
    color: gray;
    transition: color 0.3s ease;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.liked i {
    color: red;
}

.like-count {
    font-weight: bold;
}
</style>