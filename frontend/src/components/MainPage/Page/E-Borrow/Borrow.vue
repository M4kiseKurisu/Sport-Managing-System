<template>
    <div class="searchTitle">
        <div class="searchTip">搜索器材类别：</div>
        <div class="searchBox">
            <el-input v-model="keyword" placeholder="输入查询器材名"></el-input>
        </div>
        <el-button @click="search">查 询</el-button>
    </div>

    <el-row v-for="(group, index) in groups" :gutter="20" :key="index">
        <el-col v-for="(item, i) in group" :key="item.eid" :span="6">
            <div class="card">
                <EquipmentCard :url="'http://127.0.0.1:8000' + item.pic" :titleStr="item.category"
                    :contentStr="contentStrs[random()]" :amount="item.amount" />
            </div>
        </el-col>
    </el-row>
</template>

<script>
import EquipmentCard from '../../Components/EquipmentCard.vue';
import axios from 'axios'
export default {
    data() {
        return {
            keyword: "",

            contentStrs: [
                "\"我可以接受失败，人人都有失败的时候。但我不能接受未尝试过。\" - 迈克尔·乔丹",
                "\"我并非天生就是个冠军。我是通过艰苦卓绝的努力变成冠军的。\" - 莫罕默德·阿里",
                "\"跑步能教给人们不屈不挠的毅力以及怎样去面对生活的挑战。\" - 金·杜尔森",
                "\"体育不只是生理上的挑战，它还是对决心和抗压能力的最大测试。\" - 艾勒·格林斯潘",
                "\"我们学到更多的是从失败中，而不是从胜利。\" - 乔·帕切诺",
                "\"运动是生命的最佳学校之一，成败在于自我，而非他人。\" - 安德烈·毛罗瓦",
            ],

            list: []
        }
    },
    methods: {
        random() {
            let num = (Math.floor(Math.random() * 100) + 1) % 6;
            return num;
        },
        search() {
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/api/equipment/view",
                params: {
                    keyword: this.keyword
                }
            }).then((result) => {
                if (result.data.status) {
                    this.list = result.data.list
                }
            });
        }
    },
    created() {

        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/equipment/view"
        }).then((result) => {
            if (result.data.status) {
                this.list = result.data.list
            }
        });
    },
    computed: {
        groups() {
            let groups = [];
            for (let i = 0; i < this.list.length; i += 4) {
                groups.push(this.list.slice(i, i + 4));
            }
            return groups;
        },
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