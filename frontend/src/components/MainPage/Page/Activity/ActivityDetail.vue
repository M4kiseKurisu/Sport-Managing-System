<template>
    <!-- 界面标题 -->
    <div class="title">
        <!-- <div>活动详情</div> -->
        <div>{{ this.data.activity_name }}</div>
    </div>

    <el-row>

        <!-- 左侧：基本信息 -->
        <el-col :span="17">

            <!-- 上边栏：活动照片+活动基本信息 -->
            <div class="up">

                <!-- 上左侧：活动照片 -->
                <div class="pic">
                    <img :src="'http://127.0.0.1:8000' + this.data.picture" class="image">
                </div>

                <!-- 上右侧：基本信息 -->
                <div class="information">

                    <div class="subTitle">活动基本信息</div>
                    <!-- <div class="row">
                        <div class="sign">
                            <el-icon>
                                <Document />
                            </el-icon>
                        </div>
                        <div class="text">活动名称：{{ this.data.activity_name }}</div>
                    </div> -->

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <SetUp />
                            </el-icon>
                        </div>
                        <div class="text">创建者类型：{{ this.data.type }}</div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <User />
                            </el-icon>
                        </div>
                        <div class="text">创建者：{{ this.data.type === '团体' ? this.data.group_name : this.data.user_name }}
                        </div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <Compass />
                            </el-icon>
                        </div>
                        <div class="text">活动类型：{{ this.data.category }}</div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <Guide />
                            </el-icon>
                        </div>
                        <div class="text">
                            活动标签：
                            <el-tag class="category-tag" v-for="(item, index) in this.data.tags" :key="index" plain>{{ item
                            }}</el-tag>
                        </div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <Odometer />
                            </el-icon>
                        </div>
                        <div class="text">参与人数：{{ this.data.capacity }} / {{ this.data.maximum }}</div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <AlarmClock />
                            </el-icon>
                        </div>
                        <div class="text">开始时间：{{ this.data.start_time }}</div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <AlarmClock />
                            </el-icon>
                        </div>
                        <div class="text">结束时间：{{ this.data.end_time }}</div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <Location />
                            </el-icon>
                        </div>
                        <div class="text">活动地点：{{ this.data.location }}</div>
                    </div>

                    <div class="row">
                        <div class="sign">
                            <el-icon>
                                <Star />
                            </el-icon>
                        </div>
                        <div class="text">喜欢数：{{ this.data.favors }}</div>
                    </div>

                </div>

            </div>

            <hr class="divider">

            <!-- 下侧：活动简介 -->
            <div class="down">
                <div class="subTitle">活动简介</div>
                <div class="desc">{{ this.data.desc }}</div>
            </div>

        </el-col>

        <!-- 竖向分割线 -->
        <el-col :span="1">
            <div class="divider_column"></div>
        </el-col>


        <!-- 右侧：参与用户信息 -->
        <el-col :span="6">
            <div class="right">
                <div class="subTitle">参加用户</div>

                <FriendShow v-for="(item, index) in this.data.participants" :key="index" :participant="item" />
            </div>
        </el-col>

    </el-row>
</template>

<script>
import axios from 'axios'
import FriendShow from '../../Components/FriendShow.vue'
import { Document, SetUp, User, Compass, Guide, Odometer, AlarmClock, Location, Star } from "@element-plus/icons-vue";
export default {
    data() {
        return {
            aid: '',
            data: '',
            picture: '',
        }
    },
    mounted() {
        console.log(this.$route.params.aid)
        this.aid = this.$route.params.aid

        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/activity/detail",
            params: {
                aid: this.aid
            }
        }).then((result) => {
            if (result.data.status) {
                this.data = result.data.data;
            }
        });
    },
    components: {
        FriendShow,
        Document,
        SetUp,
        User,
        Compass,
        Guide,
        Odometer,
        AlarmClock,
        Location,
        Star
    }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 40px;
    margin-top: 16px;
    margin-left: 35%;
    font-size: 30px;
    font-weight: bold;
    color: rgb(11, 11, 141);
}

.up {
    display: flex;
}

.pic {
    width: 60%;
    overflow: hidden;
    position: relative;
    display: inline-block;
}

.image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.information {
    margin-left: 5%;

}

.subTitle {
    font-size: 18px;
    font-weight: bold;
    text-decoration: underline;
    margin-bottom: 16px;
}

.row {
    display: flex;
    margin-top: 8px;
}

.sign {
    margin-top: 2px;
    margin-right: 10px;
}

.text {
    font-size: 16px;
}

.category-tag {
    margin-right: 8px;
}

.divider {
    margin-top: 20px;
    color: gray;
}

.down {
    margin-top: 20px;
}

.desc {
    margin-top: 16px;
    margin-left: 6%;
    margin-right: 6%;
}

.divider_column {
    width: 1px;
    height: 100%;
    background-color: gray;
    margin-left: 0px;
}
</style>