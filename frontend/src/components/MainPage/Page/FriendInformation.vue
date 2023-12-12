<template>
  <div>
    <!-- 好友列表逻辑 -->
    <div class="centered-content">
      <el-row>
        <el-col v-for="(friend, index) in filteredFriends" :key="index">
          <FriendCard :user="friend" />
        </el-col>
      </el-row>
    </div>

    <!-- 分页逻辑 -->
    <el-pagination :small="small" :disabled="disabled" :background="background" layout="prev, pager, next" :page-size="4"
      :total="totalPages" v-model:current-page="currentPage" @current-change="handleCurrentChange" />

    <!-- 添加按钮 -->
    <el-tooltip class="box-item" effect="dark" content="添加好友" placement="left">
      <div class="add-icon" @click="openDialog">
        <el-icon>
          <circle-plus-icon />
        </el-icon>
      </div>
    </el-tooltip>

    <!-- 添加逻辑 -->
    <el-dialog v-model="dialogVisible" @close="closeDialog">
      <h2 class="custom-title">添加好友</h2>
      <AddFriendDialog></AddFriendDialog>
    </el-dialog>

    <!-- 处理按钮 -->
    <el-tooltip class="box-item" effect="dark" content="处理你的好友申请" placement="left">
      <div class="bell-icon" @click="openRequestDialog">
        <el-icon>
          <Bell />
        </el-icon>
      </div>
    </el-tooltip>

    <!-- 处理逻辑 -->
    <el-dialog v-model="requestDialogVisible" @close="closeRequestDialog">
      <h2 class="custom-title">好友申请</h2>
      <el-menu :default-active="activeTab" mode="horizontal" @select="handleMenuSelect">
        <el-menu-item index="pending">新的好友</el-menu-item>
        <el-menu-item index="receive">你的申请</el-menu-item>
      </el-menu>
      <Pending v-if="activeTab === 'pending'" />
      <Receive v-if="activeTab === 'receive'" />
    </el-dialog>
  </div>
</template>

<script lang="js">
import axios from 'axios'
import { Plus, Bell } from '@element-plus/icons-vue'
import AddFriendDialog from './Friend/AddFriend.vue'
import Pending from './Friend/Pending.vue'
import Receive from './Friend/Receive.vue'
import FriendCard from '../Components/FriendCard.vue'

export default {
  data ()
  {
    return {
      friends: [],
      newFriends: [],
      small: false,
      background: false,
      disabled: false,
      currentPage: 1,
      msg: "",
      defaultImage: "./src/images/group-default-picture.png",
      keyword: "",
      dialogVisible: false,
      requestDialogVisible: false,
      activeTab: 'pending',
      Plus,
      Bell
    }
  },
  components: {
    CirclePlusIcon: Plus,
    Bell,
    AddFriendDialog,
    Pending,
    Receive,
    FriendCard
  },
  created ()
  {
    this.getData();
  },
  computed: {
    totalPages ()
    {
      return Math.ceil( this.friends.length );
    },
    filteredFriends ()
    {
      const startIndex = ( this.currentPage - 1 ) * 4; // 每页显示 6 个好友信息
      const endIndex = startIndex + 4;

      return this.friends.slice( startIndex, endIndex );
    },
  },

  methods: {
    getData ()
    {
      axios( {
        method: "GET",
        url: "http://127.0.0.1:8000/api/friend/list",
        params: {
          uid: sessionStorage.getItem( 'uid' )
        }
      } ).then( ( result ) =>
      {
        if ( result.data.status )
        {
          this.friends = result.data.list; // 将后端数据赋值给 friends
          this.msg = result.data.msg;
        }
      } ).catch( ( error ) =>
      {
        console.error( 'Error fetching group data:', error );
      } );
    },

    handleCurrentChange ( val )
    {
      console.log( `current page: ${ val }` );
      if ( val >= 1 && val <= this.totalPages )
      {
        this.currentPage = val;
      }
    },

    search ()
    {
      axios( {
        method: "GET",
        url: "http://127.0.0.1:8000/api/user/find",

        params: {
          uid: sessionStorage.getItem( 'uid' ),
          keyword: this.keyword
        }
      } ).then( ( result ) =>
      {
        if ( result.data.status )
        {
          this.friends = result.data.list;
          this.msg = result.data.msg;
        }
      } );
    },

    openDialog ()
    {

      this.dialogVisible = true;
    },

    closeDialog ()
    {
      this.dialogVisible = false;
      this.newFriends = [];
      this.searchKeyword = '';
      this.getData()
    },

    openRequestDialog ()
    {
      this.requestDialogVisible = true;
    },

    closeRequestDialog ()
    {
      this.requestDialogVisible = false;
      this.getData()
    },

    handleMenuSelect ( index )
    {
      this.activeTab = index;
    },
  }
}

</script>

<style scoped>
.centered-content {
  padding: 0 60px;
  /* 左右空间 */

}

.friend-info {
  display: flex;
  align-items: center;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.searchTitle {
  width: 1000px;
  display: flex;
  align-items: center;
}

.searchBox {
  width: 250px;
}

.searchButton {
  width: 50px;
}

.add-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  background-color: yellow;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  z-index: 999;
  /* 确保图标在最上层 */
}

.bell-icon {
  position: fixed;
  bottom: 90px;
  right: 20px;
  width: 60px;
  height: 60px;
  background-color: rgb(106, 166, 245);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  z-index: 999;
}

.custom-title {
  text-align: center;
  /* 文本居中对齐 */
  font-size: 24px;
  /* 根据需要设置合适的字体大小 */
  color: #333;
  /* 文本颜色 */
  /* 可以根据需要添加其他样式，比如字体样式、字重等 */
}

.el-pagination {
  font-size: 25px;
  /* 调整分页器的字体大小 */
  position: fixed;
  /* 使分页器固定 */
  bottom: 10%;
  /* 确保分页器位于页面底部 */
  left: 50%;
  /* 调整分页器水平位置 */
  transform: translateX(-50%);
  z-index: 1000;
  /* 可以调整分页器的 z-index 以确保它在其他内容上方 */
}
</style>
