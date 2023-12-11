<template>
    <!-- 界面最上方活动走马灯 -->

    <el-carousel :autoplay="false" type="card" height="200px">
        <el-carousel-item v-for="item in this.prefer" :key="item.aid">
            <!-- <h3 text="2xl" justify="center">{{ item }}</h3> -->
            <img :src="'http://127.0.0.1:8000' + item.picture" class="image">
        </el-carousel-item>
    </el-carousel>

    <div class="title">
        <div>近期活动</div>
    </div>

    <div class="header">
        <!-- 选择是个人项目还是团体项目 -->

        <!-- <el-link style="font-size: 16px; ">个人活动</el-link>
        <el-divider direction="vertical" />
        <el-link style="font-size: 16px;">集体活动</el-link>
        <el-divider direction="vertical" /> -->

        <div class="search">
            <div>组织类型：</div>
            <div class="form">
                <el-select v-model="foundType" placeholder="选择组织类型">
                    <el-option v-for="item in FoundTypeOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
            </div>
        </div>

        <!-- 根据名字进行活动搜索 -->
        <div class="search">
            <div>活动名称：</div>
            <div class="form">
                <el-input v-model="input" placeholder="输入查询活动名"></el-input>
            </div>
        </div>

        <div class="longSearch">
            <div>活动日期：</div>
            <div>
                <el-date-picker class="el-date-editor" v-model="time" type="date" placeholder="选择日期" format="YYYY-MM-DD"
                    value-format="YYYY-MM-DD" />
            </div>
        </div>

        <div class="search">
            <div>活动类型：</div>
            <div class="form">
                <el-select v-model="category" placeholder="选择活动类型">
                    <el-option v-for="item in categoryOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
            </div>
        </div>

        <!-- <div class="search">
            <div>活动标签：</div>
            <div class="form">
                <el-select v-model="tag" placeholder="选择活动标签">
                    <el-option v-for="item in tagOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
            </div>
        </div> -->

        <div class="search">
            <div>活动标签：</div>
            <div class="form">
                <el-input v-model="tag" placeholder="输入活动标签"></el-input>
            </div>
        </div>

        <el-button @click="reShow()">查 询</el-button>
    </div>


    <!-- 整体活动列表 -->
    <!-- 设计：每一个版面拥有9个单项活动展示 -->

    <el-row v-for="(group, index) in groups" :gutter="20" :key="index">
        <el-col v-for="item in group" :key="item.aid" :span="8">
            <!-- 单项活动展示 1-->
            <div class="activity">
                <ActivityShow :information="item" />
            </div>
        </el-col>
    </el-row>

    <!-- 最下方需要实现换页功能，查看更多的活动，使用分页器元素 -->

    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="this.list.length" @current-change="handlePageChange" />
    </div>
</template>

<script>
import axios from 'axios';
import ActivityShow from "../../Components/ActivityShow.vue";
export default {
    data() {
        return {
            input: "",
            list: [],
            current_page: 1,
            FoundTypeOptions: [
                {
                    label: "个人创建",
                    value: 0
                },
                {
                    label: "团体创建",
                    value: 1
                }
            ],
            foundType: "",
            time: "",
            categoryOptions: [],
            category: '',
            tag: '',
            prefer: [],
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
            this.current_page = pageNo;
        },
        reShow() {
            // let search = {
            //     uid: JSON.parse(sessionStorage.getItem("uid"))
            // };
            let search = {
                uid: JSON.parse(sessionStorage.getItem("uid"))
            };
            if (this.time != "") {
                search.time = this.time
            }
            if (this.input != "") {
                search.input = this.input
            }
            if (this.category != "") {
                search.category = this.category
            }
            if (this.tag != "") {
                search.tag = this.tag
            }
            if (this.foundType != "") {
                search.type = this.foundType
            } else {
                search.type = 2
            }

            console.log(search);

            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/activity/view/active",
                params: search
            }).then((result) => {
                if (result.data.status) {
                    this.list = result.data.list;
                    this.categoryOptions = [];
                    for (let i = 0; i < this.list.length; i++) {
                        let category = {
                            label: this.list[i].category,
                            value: this.list[i].category,
                        }
                        if (!this.categoryOptions.includes(category)) {
                            this.categoryOptions.push(category);
                        }
                    }
                }
            });


            this.current_page = 1;

        }
    },
    mounted() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/activity/view/active",
            params: {
                uid: JSON.parse(sessionStorage.getItem("uid")),
                type: 2,
            },
        }).then((result) => {
            console.log(result);
            if (result.data.status) {
                this.list = result.data.list;
                this.categoryOptions = [];
                for (let i = 0; i < this.list.length; i++) {
                    let category = {
                        label: this.list[i].category,
                        value: this.list[i].category,
                    }
                    if (!this.categoryOptions.includes(category)) {
                        this.categoryOptions.push(category);
                    }
                }
            }
        });

        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/activity/recommend",
            params: {
                uid: JSON.parse(sessionStorage.getItem("uid")),
            },
        }).then((result) => {
            if (result.data.status) {
                this.prefer = result.data.list;
            }
        })
    },
    computed: {
        groups() {
            let groups = [];
            for (let i = (this.current_page - 1) * 9; i < this.current_page * 9; i += 3) {
                groups.push(this.list.slice(i, i + 3));
            }
            return groups;
        }
    }
}
</script>
  
<style scoped>
.image {
    object-fit: cover;
    width: 100%;
    height: 100%;
}

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
    width: 220px;
    display: flex;
    align-items: center;
    margin-right: 10px;
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

.form {
    width: 140px;
}

.form .el-date-editor {
    --el-date-editor-width: 140px !important;
    width: 140px !important;
}

.longSearch {
    display: flex;
    align-items: center;
    margin-right: 10px;
}
</style>