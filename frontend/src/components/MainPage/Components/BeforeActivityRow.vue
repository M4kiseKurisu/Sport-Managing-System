<template>
    <div class="all">
        <!-- 左侧图片 -->
        <div class="pic">
            <el-tag class="category-tag" effect="dark" size="large">{{ information.category }}</el-tag>
            <el-tag class="additional-tag" effect="dark" size="large" color="#FFA500">{{ information.type }}</el-tag>
            <el-tag v-if="information.is_joined" class="additional-tag2" effect="dark" size="large"
                type="success">已参与</el-tag>
            <el-tag v-else class="additional-tag2" effect="dark" size="large" type="info">未参与</el-tag>
            <img :src="this.picture" class="image">
            <div class="text-overlay">
                {{ information.name }}
            </div>
            <div class="likes-container">
                <!-- <button class="likes-icon" :class="{ 'liked': liked }" @click="toggleLike()">
                    <span v-if="liked">❤️</span>
                    <span v-else>🤍</span>
                </button> -->
                <span class="likes-icon">❤️</span>
                <span class="likes-count">{{ information.favor }}</span>
            </div>
            <div class="image-caption">
                参与人数：{{ information.capacity }} / {{ information.maximum }}
            </div>
        </div>


        <!-- 右侧信息 -->
        <div class="right">
            <div class="text">开始时间：{{ information.start_time }}</div>
            <div class="text">结束时间：{{ information.end_time }}</div>
            <div class="button">
                <el-button type="primary" plain @click="checkInformation()">查看详情</el-button>
            </div>
        </div>

    </div>
</template>
  
<script>
import axios from 'axios'
export default {
    data() {
        return {
            picture: '',
            aid: '',
            liked: false,
        }
    },
    props: {
        information: {
            type: Object,
            required: true
        }
    },
    mounted() {
        this.picture = "http://127.0.0.1:8000" + this.information.picture;
        this.aid = this.information.aid;
    },
    methods: {
        checkInformation() {
            this.$router.push('/Page/Activity_Information/Detail/' + this.aid);
        },
        toggleLike() {
            if (this.liked) {
                let liking = {
                    uid: JSON.parse(sessionStorage.getItem("uid")),
                    aid: this.aid,
                    method: "remove"
                }
                //取消点赞
                axios({
                    method: "POST",
                    url: "http://127.0.0.1:8000/api/activity/favor",
                    data: liking
                })
            }

            else {
                let liking = {
                    uid: JSON.parse(sessionStorage.getItem("uid")),
                    aid: this.aid,
                    method: "like"
                }
                //点赞
                axios({
                    method: "POST",
                    url: "http://127.0.0.1:8000/api/activity/favor",
                    data: liking
                })
            }

            this.liked = !this.liked;
        }
    }
}
</script>
  
<style scoped>
.all {
    display: flex;
    width: 90%;
    margin-left: 5%;
    border-right: 4px solid #4c82ff63;
    border-bottom: 4px solid #4c82ff63;
    border-radius: 10px;
}

.text {
    font-size: 18px;
}

.pic {
    width: 70%;
    height: 200px;
    overflow: hidden;
    position: relative;
    display: inline-block;
}

.image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: blur(3px);
}

.text-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background-color: rgba(0, 0, 0, 0.2);
    /* 设置叠加的背景颜色和透明度 */
    color: #ffffff;
    /* 设置文字颜色 */
    font-size: 30px;
    font-weight: bold;
}

.likes-container {
    position: absolute;
    bottom: 10px;
    left: 10px;
    display: flex;
    align-items: center;
    color: #ffffff;
}

.likes-icon {
    font-size: 18px;
    margin-right: 5px;
    border: none;
    background-color: transparent;
    padding: 0;
    cursor: pointer;
    margin-top: -2px;
}

.likes-icon:focus {
    outline: none;
}

.likes-icon span {
    font-size: 18px;
}

.likes-icon.liked span {
    color: red;
}

.likes-count {
    font-size: 16px;
}

.category-tag {
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 2;
}

.el-tag {
    font-size: 16px;
}

.right {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-left: 5%;
}

.additional-tag {
    position: absolute;
    top: 10px;
    left: calc(75px);
    /* 调整标签之间的间距 */
    z-index: 2;
}

.additional-tag2 {
    position: absolute;
    top: 10px;
    left: calc(140px);
    /* 调整标签之间的间距 */
    z-index: 2;
}

.image-caption {
    position: absolute;
    bottom: 10px;
    right: 10px;
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
}

.button {
    margin-top: 15px;
}

.likes-icon.liked {
    color: red;
}
</style>