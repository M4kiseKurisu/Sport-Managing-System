<template>
    <el-row>

        <!-- 左侧信息 -->
        <el-col :span="14">
            <div>

                <div class="formItem">
                    <div class="formTip">创建类型：</div>
                    <div class="formInput">
                        <el-select v-model="fondType" placeholder="选择创建类型">
                            <el-option v-for="item in fondTypes" :key="item.value" :label="item.label"
                                :value="item.value" />
                        </el-select>
                    </div>

                    <div class="formTip">选择团体：</div>
                    <div class="formInput">
                        <el-select v-model="fondGroup" placeholder="选择创建团体" v-if="fondType === '1'">
                            <el-option v-for="item in fondGroups" :key="item.value" :label="item.label"
                                :value="item.value" />
                        </el-select>
                        <el-select v-model="fondGroup" placeholder="选择创建团体" disabled v-else>
                        </el-select>
                    </div>
                </div>

                <div class="formItem">
                    <div class="formTip">活动名称：</div>
                    <div class="formInput">
                        <el-input v-model="name" placeholder="输入活动名称" />
                    </div>
                </div>

                <div class="formItem">
                    <div class="formTip">活动类型：</div>
                    <div class="formInput">
                        <el-select v-model="category" placeholder="选择活动类型">
                            <el-option v-for="item in categories" :key="item.value" :label="item.label"
                                :value="item.value" />
                        </el-select>
                    </div>
                </div>

                <div class="formItem">
                    <div class="formTip">活动标签：</div>
                    <div class="formTip" v-for="item in tags" :key="item.value">
                        <el-tag>{{ item.value }}</el-tag>
                    </div>
                    <div class="formInput">
                        <el-input v-model="tagName" placeholder="输入标签名称" />
                    </div>
                    <div class="formTip">
                        <el-button type="primary" plain @click="addTag()">点击添加</el-button>
                    </div>
                </div>

                <div class="formItem">
                    <div class="formTip">最大人数：</div>
                    <div class="formInput">
                        <el-input-number v-model="maximum" :min="1" :max="10000" />
                    </div>
                </div>

                <div class="formItem">
                    <div class="formTip">是否公开：</div>
                    <div class="formInput">
                        <el-radio-group v-model="private">
                            <el-radio-button label="公开" />
                            <el-radio-button label="私人" />
                        </el-radio-group>
                    </div>
                </div>

                <div class="formItem">
                    <div class="formTip">活动描述：</div>
                    <div class="desc">
                        <el-input v-model="desc" placeholder="输入活动描述" :rows="5" type="textarea" />
                    </div>
                </div>

            </div>

            <!-- <hr class="divider"> -->
        </el-col>

        <!-- 右侧信息 -->
        <el-col :span="10">

            <div>
                <div class="formItem">
                    <div class="formTip">选择图片：</div>
                    <div class="formTip">
                        <el-upload v-model:file-list="this.fileList" :limit="1" :show-file-list="false" :auto-upload="false"
                            action="#">
                            <el-button type="primary" plain>选择图片</el-button>
                        </el-upload>
                    </div>
                    <div class="formTip">
                        <el-button type="primary" @click="uploadPic()">更新图片</el-button>
                    </div>
                </div>
            </div>

            <div v-if="this.pic" class="formItem">
                <img :src="this.pic" class="image">
            </div>

            <div>
                <div class="nextstep">
                    <div class="formTip">
                        <el-button type="primary" @click="toNextStep">去选择场地</el-button>
                    </div>
                </div>
            </div>

        </el-col>
    </el-row>

    <!-- <div class="formItem">
        <div class="formTip">选择场地：</div>
        <div class="formItem">
            <el-select v-model="fieldCategory" placeholder="选择场地类型">
                <el-option v-for="item in fieldCategories" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
        </div>
    </div> -->
</template>

<script>
import axios from "axios"
import dayjs from 'dayjs'
export default {
    data() {
        return {
            fondType: '',
            fondTypes: [
                {
                    label: "个人创建",
                    value: "0"
                },
                {
                    label: "团体创建",
                    value: "1"
                }
            ],
            fondGroup: '',
            fondGroups: [],
            name: '',
            category: '',
            categories: [
                {
                    label: "篮球",
                    value: "篮球"
                },
                {
                    label: "足球",
                    value: "足球"
                },
                {
                    label: "跑步",
                    value: "跑步"
                },
                {
                    label: "impart",
                    value: "impart"
                },
            ],
            tagName: '',
            tags: [],
            maximum: '',
            private: '',
            fileList: [],
            pic: '',
            desc: '',
            fieldCategory: '',
            fieldCategories: [],
        }
    },
    methods: {
        addTag() {
            if (this.tagName != '') {
                this.tags.push({
                    value: this.tagName
                });
                this.tagName = '';
                this.$message({
                    showClose: true,
                    message: "已经成功添加标签",
                    type: 'success'
                });
            } else {
                this.$message({
                    showClose: true,
                    message: "添加标签失败",
                    type: 'error'
                });
            }
        },
        uploadPic() {
            console.log("hello")
            const file = this.fileList[0].raw;
            const reader = new FileReader();



            reader.onload = () => {
                this.pic = reader.result;  // 将图片 URL 存储到数据属性中
            };

            reader.readAsDataURL(file);  // 使用 Data URL 将文件读取为图片 URL

            console.log(this.pic);
        },
        toNextStep() {
            if (this.fondType != ''
                && ((this.fondType === '1' && this.fondGroup != '') || this.fondType === '0')
                && this.name != ''
                && this.category != ''
                && this.tags != []
                && (this.maximum != '' && this.maximum > 0)
                && this.private != ''
                && this.desc != ''
                && this.pic != '') {

                let allTags = this.tags[0].value;
                for (let i = 1; i < this.tags.length; i++) {
                    allTags += ("-" + this.tags[i].value);
                }

                let start = this.date + " " + this.startTime;
                let end = this.date + " " + this.endTime;

                console.log(allTags);
                console.log(this.fondType);
                console.log(this.fondGroup);

                this.$emit("returnData", {
                    status: true,
                    information: {
                        type: this.fondType,
                        gid: this.fondGroup,
                        name: this.name,
                        desc: this.desc,
                        category: this.category,
                        tags: allTags,
                        maximum: this.maximum,
                        private: (this.private === '公开') ? false : true,
                        picture: this.fileList[0].raw
                    },
                    msg: "活动申请基本信息录入成功"
                })
            }

            else if (this.maximum == 0) {
                this.$emit("returnData", {
                    status: false,
                    information: null,
                    msg: "活动最大人数至少为1人！"
                })
            }

            else {
                this.$emit("returnData", {
                    status: false,
                    information: null,
                    msg: "有条目未填写！"
                })
            }
        },
        updateDatePicker() {
            this.$nextTick(() => {
                // 更新日期选择框
                // 可以在这里执行其他逻辑
            });
        }
    },
    created() {
        //获取此用户所属且为管理员/创建者的group
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/user/group",
            params: {
                uid: JSON.parse(sessionStorage.getItem('uid'))
            }
        }).then((result) => {
            if (result.data.status) {
                this.fondGroups = [];
                for (let i = 0; i < result.data.list.length; i++) {
                    if (result.data.list[i].type === '创建人' || result.data.list[i].type === '管理员') {
                        this.fondGroups.push({
                            value: result.data.list[i].gid,
                            label: result.data.list[i].group_name,
                        });
                    }
                }
            }
        });
    }
}
</script>

<style scoped>
.title {
    font-size: 20px;
    margin-bottom: 16px;
    margin-top: 16px;
}

.formItem {
    display: flex;
    align-items: center;
    margin-top: 10px;
    margin-bottom: 10px;
}

.formTip {
    font-size: 16px;
    margin-right: 12px;
}

.formInput {
    margin-right: 24px;
}

.image {
    width: 320px;
    height: 250px;
    object-fit: contain;
}

.desc {
    width: 555px;
}

.divider {
    color: lightgray;
    margin-top: 30px;
    margin-bottom: 10px;
    width: 80%;
}

.nextstep {
    margin-top: 30px;
    margin-right: 20%;
    display: flex;
    justify-content: flex-end;
}
</style>