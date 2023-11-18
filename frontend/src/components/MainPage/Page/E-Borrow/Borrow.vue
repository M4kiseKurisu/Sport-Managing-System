<template>
    <div class="searchTitle">
        <div class="searchTip">搜索器材类别：</div>
        <div class="searchBox">
            <el-input v-model="search" placeholder="输入查询器材名"></el-input>
        </div>
        <el-button>查 询</el-button>
    </div>

    <el-row :gutter="20">
        <el-col :span="6">
            <div class="card">
                <EquipmentCard v-if="this.have1" :url="url1" :titleStr="titleStr1" :contentStr="contentStr1"
                    :amount=amount1 />
            </div>
            <div class="card">
                <EquipmentCard v-if="this.have5" :url="url1" :titleStr="titleStr1" :contentStr="contentStr5"
                    :amount=amount1 />
            </div>
        </el-col>

        <el-col :span="6">
            <div class="card">
                <EquipmentCard v-if="this.have2" :url="url1" :titleStr="titleStr1" :contentStr="contentStr2"
                    :amount=amount1 />
            </div>
            <div class="card">
                <EquipmentCard v-if="this.have6" :url="url1" :titleStr="titleStr1" :contentStr="contentStr6"
                    :amount=amount1 />
            </div>
        </el-col>

        <el-col :span="6">
            <div class="card">
                <EquipmentCard v-if="this.have3" :url="url1" :titleStr="titleStr1" :contentStr="contentStr3"
                    :amount=amount1 />
            </div>
        </el-col>

        <el-col :span="6">
            <div class="card">
                <EquipmentCard v-if="this.have4" :url="url1" :titleStr="titleStr1" :contentStr="contentStr4"
                    :amount=amount1 />
            </div>
        </el-col>
    </el-row>
</template>

<script>
import EquipmentCard from '../../Components/EquipmentCard.vue';
export default {
    data() {
        return {
            search: "",

            have1: true,
            have2: true,
            have3: true,
            have4: true,
            have5: true,
            have6: true,

            contentStr1: "\"我可以接受失败，人人都有失败的时候。但我不能接受未尝试过。\" - 迈克尔·乔丹",
            contentStr2: "\"我并非天生就是个冠军。我是通过艰苦卓绝的努力变成冠军的。\" - 莫罕默德·阿里",
            contentStr3: "\"跑步能教给人们不屈不挠的毅力以及怎样去面对生活的挑战。\" - 金·杜尔森",
            contentStr4: "\"体育不只是生理上的挑战，它还是对决心和抗压能力的最大测试。\" - 艾勒·格林斯潘",
            contentStr5: "\"我们学到更多的是从失败中，而不是从胜利。\" - 乔·帕切诺",
            contentStr6: "\"运动是生命的最佳学校之一，成败在于自我，而非他人。\" - 安德烈·毛罗瓦",


            url1: "../../../images/basketball.png",
            titleStr1: "篮球",
            amount1: 10,
        }
    },
    components: {
        EquipmentCard,
    }
}
</script>

<style scoped>
.searchTitle {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.searchTip {
    font-size: 16px;
    margin-right: 20px;
}

.searchBox {
    width: 240px;
}

.card {
    margin-top: 30px;
}
</style>