<template>
    <!-- 界面标题 -->
    <div class="title">
        <div>过往活动</div>
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
            <div>排序方式：</div>
            <div class="form">
                <el-select v-model="method" placeholder="选择排序方式">
                    <el-option v-for="item in methodOptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
            </div>
        </div>

        <el-button @click="reShow()">查 询</el-button>
    </div>

    <!-- 表项 -->
    <div class="showform">
        <BeforeActivityRow v-for="(item, index) in groups" :key="index" :information="item" />
    </div>

    <!-- 换页器 -->
    <div class="pagination">
        <el-pagination background layout="prev, pager, next" :total="this.list.length" @current-change="handlePageChange" />
    </div>
</template>

<script>
import axios from 'axios'
import BeforeActivityRow from '../../Components/BeforeActivityRow.vue';
export default {
    data() {
        return {
            current_page: 1,
            list: [],
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
            methodOptions: [
                {
                    label: "时间顺序",
                    value: "time"
                },
                {
                    label: "点赞数顺序",
                    value: "favor"
                },
                {
                    label: "规模顺序",
                    value: "scale"
                }
            ],
            method: "",
            time: "",
            categoryOptions: [],
            category: '',
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
                this.categoryOptions = [];
                if (result.data.status) {
                    this.list = result.data.list;
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
        },
        handlePageChange(pageNo) {
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
            if (this.foundType != "") {
                search.type = this.foundType
            } else {
                search.type = 2
            }
            if (this.method != "") {
                search.method = this.method
            } else {
                search.method = "time"
            }

            console.log(search);

            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/activity/view/inactive",
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
    created() {
        this.draw()
    },
    components: { BeforeActivityRow },
    computed: {
        groups() {
            let end = this.list.length < 6 * this.current_page ? this.list.length : 6 * this.current_page;
            return this.list.slice(6 * (this.current_page - 1), end);
        }
    }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.header {
    display: flex;
    align-items: center;
}

.search {
    width: 220px;
    display: flex;
    align-items: center;
    margin-right: 10px;
}

.form {
    width: 140px;
}

.longSearch {
    display: flex;
    align-items: center;
    margin-right: 10px;
}

.row {
    width: 60%;
    height: 200px;
}

.showform {
    margin-top: 20px;
}

.pagination {
    display: flex;
    justify-content: flex-end;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-right: 7%;
}
</style>