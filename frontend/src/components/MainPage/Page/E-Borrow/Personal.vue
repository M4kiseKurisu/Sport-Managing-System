<template>
  <div class="headline">
    <div class="title">
      <div>个人借出</div>
    </div>

    <div class="search">
      <BorrowSearch :isGroup="false" @someEvent="getHandle" />
    </div>
  </div>

  <BorrowFormRow :isTitle="true" :isGroup="false" />
  <!-- <BorrowFormRow v-if="have1" :information="list[0]" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have2" :information="information2" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have3" :information="information3" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have4" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have5" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have6" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have7" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have8" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have9" :information="information1" :isTitle=false :isGroup=false />
    <BorrowFormRow v-if="have10" :information="information1" :isTitle=false :isGroup=false /> -->
  <BorrowFormRow v-for="(item, index) in groups" :key="index" :information="item" :isTitle="false" :isGroup="false" />
  <div class="pagination">
    <el-pagination background layout="prev, pager, next" :total="this.list.length" @current-change="handlePageChange" />
  </div>
</template>

<script>
import BorrowFormRow from "../../Components/BorrowFormRow.vue";
import BorrowSearch from "../../Components/BorrowSearch.vue";
import axios from "axios";
export default {
  data() {
    return {
      current_page: 1,

      // have1: false,
      // have2: false,
      // have3: false,
      // have4: false,
      // have5: false,
      // have6: false,
      // have7: false,
      // have8: false,
      // have9: false,
      // have10: false,

      // information1: {
      //     name: "篮球",
      //     amount: "2",
      //     returnTime: "2023/11/20",
      //     state: "未归还",
      // },
      // information2: {
      //     name: "篮球",
      //     amount: "1",
      //     returnTime: "2023/9/7",
      //     state: "已归还",
      // },
      // information3: {
      //     name: "篮球",
      //     amount: "8",
      //     returnTime: "2023/9/5",
      //     state: "已归还",
      // },

      list: [],
      // information: {
      //     name: list[0].category,
      //     amount: list[0].lend_amount,
      //     returnTime: list[0].end_time,
      //     state: list[0].is_return,
      // }
      // params: {
      //     uid: JSON.parse(sessionStorage.getItem('uid')),
      //     config: {
      //         method: 'person',
      //         category: '',
      //         time: '',
      //         state: '',
      //     }
      // }
      message: "",
    };
  },
  components: {
    BorrowFormRow,
    BorrowSearch,
  },
  methods: {
    handlePageChange(pageNo) {
      // pageNo 是你点击的页号
      // 在这里，你可以获取该页面的数据，并更新你的组件
      // 确保你的请求是异步的，以避免阻塞用户界面
      this.current_page = pageNo;
    },
    toString() { },
    getHandle(data) {
      this.message = data;
      console.log(this.message);
      let searchUrl =
        "http://127.0.0.1:8000/api/equipment/record?uid=" +
        JSON.parse(sessionStorage.getItem("uid"));
      searchUrl += '&config={"method":"person"';
      if (data.type != "") {
        searchUrl += ', "category":"' + data.type + '"';
      }
      if (data.time != "" && data.time != null) {
        searchUrl += ', "time":"' + data.time + '"';
      }
      if (data.state == 0 || data.state == 2) {
        searchUrl += ', "state":"' + data.state + '"';
      }
      searchUrl += "}";
      console.log(searchUrl);
      axios({
        method: "GET",
        url: searchUrl,
      }).then((result) => {
        console.log(result);
        if (result.data.status) {
          // console.log(result.data.list);
          this.list = [];
          for (let i = 0; i < result.data.list.length; i++) {
            this.list.push({
              url: "http://127.0.0.1:8000" + result.data.list[i].pic,
              name: result.data.list[i].category,
              amount: String(result.data.list[i].lend_amount),
              startTime: result.data.list[i].start_time,
              returnTime: result.data.list[i].end_time,
              state: result.data.list[i].is_return,
            });
          }
        }
        console.log(this.list);
      });
    },
  },
  created() {
    console.log(JSON.parse(sessionStorage.getItem("uid")));
    let searchUrl =
      "http://127.0.0.1:8000/api/equipment/record?uid=" +
      JSON.parse(sessionStorage.getItem("uid")) +
      '&config={"method":"person"}';
    axios({
      method: "GET",
      // url: 'http://127.0.0.1:8000/api/equipment/record?uid=2135220&config={"method": "group", "time":"2023-12-12"}',
      url: searchUrl,
      // params: {
      //     uid: JSON.parse(sessionStorage.getItem('uid')),
      //     config: "{ 'method': 'person' }"
      // }
    }).then((result) => {
      if (result.data.status) {
        // console.log(result.data.list);
        for (let i = 0; i < result.data.list.length; i++) {
          this.list.push({
            url: "http://127.0.0.1:8000" + result.data.list[i].pic,
            name: result.data.list[i].category,
            amount: String(result.data.list[i].lend_amount),
            returnTime: result.data.list[i].end_time,
            state: result.data.list[i].is_return,
          });
        }
      }
    });
  },
  computed: {
    groups() {
      let end =
        this.list.length < 10 * this.current_page
          ? this.list.length
          : 10 * this.current_page;
      return this.list.slice(10 * (this.current_page - 1), end);
    },
  },
};
</script>

<style scoped>
.headline {
  display: flex;
  justify-content: space-between;
}

.title {
  font-size: 20px;
  margin-bottom: 30px;
  margin-top: 20px;
}

.search {
  display: flex;
  align-items: center;
  margin-right: 24px;
}

.pagination {
  display: flex;
  justify-content: flex-end;
  margin-top: 30px;
  margin-bottom: 30px;
  margin-right: 7%;
}
</style>