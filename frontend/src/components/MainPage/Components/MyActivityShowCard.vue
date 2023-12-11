<template>
    <div class="border">
        <div class="topic">这里是名字</div>
        <div class="text">活动时间：</div>
        <div class="text">活动类型：</div>
        <div class="text">活动标签：</div>
        <div class="buttonContainer">
            <div class="button">
                <el-button type="primary">查看详情</el-button>
                <el-button type="danger">退出/撤销活动</el-button>
            </div>
        </div>

        <div class="like-button">
            <div class="heart-icon" :class="{ 'liked': liked }" @click="toggleLike">
                <i class="fas fa-heart"></i>
            </div>
            <div class="like-count">{{ likeCount }}</div>
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            liked: false,
            likeCount: 0
        }
    },
    methods: {
        toggleLike() {
            if (this.liked) {
                this.liked = false;
                this.likeCount--;
            } else {
                this.liked = true;
                this.likeCount++;
            }
        }
    },
    props: ["name", "start_time", "end_time", "category", "tags", "favor", "aid"]
}
</script>

<style scoped>
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
    margin-bottom: 15px;
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
}

.heart-icon {
    cursor: pointer;
    width: 24px;
    height: 24px;
    margin-right: 8px;
    position: relative;
}

.heart-icon i {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    color: gray;
    transition: color 0.3s ease;
}

.liked i {
    color: red;
}

.like-count {
    font-weight: bold;
}
</style>