<template>
    <!-- 界面标题 -->
    <div class="title">
        <div>活动列表</div>
    </div>

    <!-- 界面最上方活动走马灯 -->

    <el-carousel :autoplay="false" type="card" height="200px">
        <el-carousel-item v-for="item in 6" :key="item">
            <h3 text="2xl" justify="center">{{ item }}</h3>
        </el-carousel-item>
    </el-carousel>

    <div class="title">
        <div>近期活动</div>
    </div>

    <div class="header">
        <!-- 选择是个人项目还是团体项目 -->
        <el-link style="font-size: 16px; ">个人活动</el-link>
        <el-divider direction="vertical" />
        <el-link style="font-size: 16px;">集体活动</el-link>
        <el-divider direction="vertical" />
        <!-- 根据名字进行活动搜索 -->
        <div>查询活动：</div>
        <div class="search">
            <el-input v-model="input" placeholder="输入查询活动名"></el-input>
        </div>
        <el-button>查 询</el-button>
    </div>


    <!-- 整体活动列表 -->
    <!-- 设计：每一个版面拥有9个单项活动展示 -->

    <el-row :gutter="20">
        <el-col :span="8">

            <!-- 单项活动展示 1-->
            <div class="activity">
                <ActivityShow />
            </div>

            <!-- 单项活动展示 4-->
            <div class="activity">
                <ActivityShow />
            </div>

            <!-- 单项活动展示 7-->
            <div class="activity">
                <ActivityShow />
            </div>

        </el-col>

        <el-col :span="8">

            <!-- 单项活动展示 2-->
            <div class="activity">
                <ActivityShow />
            </div>

            <!-- 单项活动展示 5-->
            <div class="activity">
                <ActivityShow />
            </div>

            <!-- 单项活动展示 8-->
            <div class="activity">
                <ActivityShow />
            </div>

        </el-col>

        <el-col :span="8">

            <!-- 单项活动展示 3-->
            <div class="activity">
                <ActivityShow />
            </div>

            <!-- 单项活动展示 6-->
            <div class="activity">
                <ActivityShow />
            </div>

            <!-- 单项活动展示 9-->
            <div class="activity">
                <ActivityShow />
            </div>

        </el-col>
    </el-row>

    <!-- 最下方需要实现换页功能，查看更多的活动，使用分页器元素 -->

    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="1000" @current-change="handlePageChange" />
    </div>
</template>

<script>
import ActivityShow from "../Components/ActivityShow.vue";
export default {
    data() {
        return {
            input: ""
        }
    },
    components: {
        ActivityShow,
    },
    methods: {
        handlePageChange(pageNo) {
            // pageNo 是你点击的页号
            // 在这里，你可以获取该页面的数据，并更新你的组件
            // 确保你的请求是异步的，以避免阻塞用户界面
        },
    }
}
</script>
  
<style scoped>
.el-row {
    margin-top: 40px;
}

.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.header {
    display: flex;
    align-items: center;
}

.activity {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

.pagination {
    display: flex;
    justify-content: flex-end;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-right: 30px;
}

.search {
    width: 200px;
    margin-left: 10px;
}

.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>