<template>
    <div class="card">
        <el-card :body-style="{}">
            <div class="title">
                <div class="size">
                    <img :src="url" class="pic" />
                </div>
                <div class="str1">{{ titleStr }}</div>
            </div>

            <div class="str2"> {{ contentStr }} </div>

            <el-divider />

            <div class="apply">
                <div>剩余数量：{{ amount }}</div>
                <div class="button">
                    <el-button @click="clickApply()"> 点击申请 </el-button>
                </div>
            </div>
        </el-card>
    </div>

    <el-dialog v-model="dialogVisible" title="申请器材" width="36%">
        <div class="text">器材类型：{{ titleStr }}</div>
        <div class="text">当前此器材剩余数量：{{ amount }}</div>

        <el-divider />

        <div style="margin-top: 6px">
            <el-radio-group v-model="radio">
                <el-radio-button label="个人申请" />
                <el-radio-button label="团体申请" />
            </el-radio-group>
        </div>

        <div class="selector">
            <div style="font-size: 16px; margin-right: 12px;">申请团体名：</div>
            <el-select v-if="this.radio === '团体申请'" v-model="value" placeholder="团体名称">
                <el-option v-for="item in list" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
            <el-select v-else v-model="value" disabled placeholder="团体名称"></el-select>
        </div>

        <div class="selector">
            <div style="font-size: 16px; margin-right: 12px;">开始时间：</div>
            <el-date-picker v-model="startTime" type="datetime" placeholder="设置开始时间" />
        </div>
        <div class="selector">
            <div style="font-size: 16px; margin-right: 12px;">结束时间：</div>
            <el-date-picker v-model="endTime" type="datetime" placeholder="设置结束时间" />
        </div>

        <div class="selector">
            <div style="font-size: 16px; margin-right: 12px;">申请数量：</div>
            <el-input-number v-model="num" :min="1" />
        </div>

        <div class="applyButton">
            <el-button type="primary" @click="submitForm()">立即申请</el-button>
        </div>
    </el-dialog>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            dialogVisible: "false",
            radio: "个人申请",
            value: "",
            num: "",
            options: [
                {
                    value: 'Option1',
                    label: 'Option1',
                },
                {
                    value: 'Option2',
                    label: 'Option2',
                },
                {
                    value: 'Option3',
                    label: 'Option3',
                },
                {
                    value: 'Option4',
                    label: 'Option4',
                },
                {
                    value: 'Option5',
                    label: 'Option5',
                },
            ],
            startTime: "",
            endTime: "",
            list: [],
        }
    },
    methods: {
        submitForm() {
            this.dialogVisible = false;
        },
        clickApply() {
            this.dialogVisible = true;
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/user/group",
                params: {
                    uid: JSON.parse(sessionStorage.getItem('uid'))
                }
            }).then((result) => {
                console.log(result.data.status);
                if (result.data.status) {
                    for (let i = 0; i < result.data.list.length; i++) {
                        this.list.push({
                            value: 'Option' + String(i + 1),
                            label: result.data.list[i].group_name,
                        });
                        console.log(result.data.list[i].group_name);
                    }
                }
            });
        },
    },
    mounted() {
        this.dialogVisible = false;
    },
    props: ["url", "titleStr", "contentStr", "amount"]
}
</script>

<style scoped>
.card {
    margin-left: 8%;
    margin-right: 8%;
}

.el-card {
    --el-card-border-radius: 10px;
    border-right: 4px solid #4c82ff63;
    border-bottom: 4px solid #4c82ff63;
}

.size {
    width: 80px;
    height: 80px;
}

.pic {
    background-repeat: no-repeat;
    background-position: center;
    object-fit: fill;
    width: 100%;
    height: 100%;
}

.title {
    display: flex;
    align-items: center;
    padding-left: 24px;
    padding-right: 16px;
}

.str1 {
    font-size: 22px;
    margin-left: 24px;
    font-weight: bold;
    margin-top: 12px;
}

.str2 {
    font-size: 16px;
    margin-left: 16px;
    margin-right: 16px;
    margin-top: 20px;
    font-style: italic;
}

.apply {
    display: flex;
    align-items: center;
    padding-left: 16px;
    padding-right: 16px;
    margin-top: 16px;
}

.button {
    margin-left: 14px;
}

.text {
    margin-top: 6px;
    font-size: 16px;
}

.selector {
    margin-top: 12px;
    display: flex;
    align-items: center;
}

.applyButton {
    margin-top: 12px;
    display: flex;
    justify-content: flex-end;
    margin-right: 10px;
}
</style>