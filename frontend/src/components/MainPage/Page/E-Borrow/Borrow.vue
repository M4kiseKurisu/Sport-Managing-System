<template>
    <el-row :gutter="20">
        <el-col :span="6">
            <div class="card">
                <EquipmentCard :url="url1" :titleStr="titleStr1" :contentStr="contentStr1" />
            </div>
        </el-col>

        <el-col :span="6"></el-col>

        <el-col :span="6"></el-col>

        <el-col :span="6"></el-col>
    </el-row>
</template>

<script>
import EquipmentCard from '../../Components/EquipmentCard.vue';
export default {
    data() {
        return {
            url1: "../../../images/basketball.png",
            titleStr1: "篮球",
            contentStr1: "\"我可以接受失败，人人都有失败的时候。但我不能接受未尝试过。\" - 迈克尔·乔丹",
        }
    },
    components: {
        EquipmentCard,
    }
}
</script>

<style scoped>
.card {
    margin-top: 30px;
}
</style>