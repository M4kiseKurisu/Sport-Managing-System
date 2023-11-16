<template>
    <!-- 本组件用来统一使用活动的总体使用布局 -->

    <div>
        <!-- 活动图片 -->
        <div class="image">
            <el-image style="width: 300px; height: 200px" src="./src/images/animelogo.png" fit="fill" />
        </div>

        <!-- 活动名称及id -->
        <div class="content">
            <div style="color: black; text-align: center;">{{ showNameInformation }}</div>
        </div>

        <!-- 活动详细内容介绍（弹出窗口） -->
        <div class="dialog">
            <el-button text @click="dialogVisible = true" style="font-size: 16px;">
                点击查看活动具体信息
            </el-button>

            <el-dialog v-model="dialogVisible" title="活动信息" width="50%" :modal="false">
                <div class="text">活动名称： {{ showIdInformation }}</div>
                <div class="text">活动ID： {{ showIdInformation }}</div>
                <div class="text">活动组织者： {{ showOrganizer }}</div>
                <div class="text">活动内容： {{ showInformation }}</div>
                <template #footer>
                    <span class="dialog-footer">
                        <el-button type="primary" @click="dialogVisible = false"> 确定 </el-button>
                    </span>
                </template>
            </el-dialog>
        </div>


    </div>
</template>

<script lang="ts">
import { ref } from 'vue'
const dialogVisible = ref(false)
export default {
    setup() {
        return {
            dialogVisible
        }
    },
    data() {
        return {
            name: "本次活动的名字",
            id: "本次活动的id",
            information: "本次活动的基本信息：balabalabalabalabalabalabalabalabalabalabalabalabalabalabalabalabalabala",
            organizer: "本次活动的策划组织或个人",
            isPrivate: false,
        }
    },
    computed: {
        showNameInformation() {
            return this.name
        },
        showIdInformation() {
            return this.id
        },
        showInformation() {
            return this.information
        },
        showOrganizer() {
            return this.organizer + " ( " + (this.isPrivate ? "本次活动是私人的" : "本次活动不是私人的") + " )"
        }
    }
}
</script>

<style scoped>
.image {
    display: flex;
    justify-content: center;
}

.content {
    display: flex;
    justify-content: center;
    font-size: 16px;
    margin-top: 12px;
    flex-direction: column;
}

.dialog {
    margin-top: 6px;
    display: flex;
    justify-content: center;
}

.text {
    margin-top: 6px;
    font-size: 16px;
}
</style>