<template>
  <div>
    <!-- 好友列表逻辑 -->
    <el-table :data="filteredFriends" style="width: 80%">
      <el-table-column label="呢称" width="200">
        <template #default="scope">
          <div v-for="friend in scope.row" :key="friend.uid" class="friend-info">
            <div v-if="friend.pic !== null">
              <img :src="'http://127.0.0.1:8000' + friend.pic" class="avatar" />
            </div>
            <div v-else>
              <img :src="defaultImage" class="avatar" />
            </div>
            <span>{{ friend.user_name }}</span>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="个性签名">
        <template #default="scope">
          <div v-for="friend in scope.row" :key="friend.uid">
            {{ friend.signature }}
          </div>
        </template>
      </el-table-column>

      <el-table-column align="right">
        <template #header>
          <div class="searchTitle">
            <div class="searchBox">
              <el-input v-model="keyword" placeholder="搜索你的好友"></el-input>
            </div>
            <el-button @click="search" class="searchButton">查询</el-button>
          </div>
        </template>
        <template #default="scope" align="center">
          <div v-for="friend in scope.row" :key="friend.uid" class="user-info">
            <el-button size="small" type="danger" @click="handleDelete(friend)">删除好友</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页逻辑 -->
    <el-pagination :small="small" :disabled="disabled" :background="background" layout="prev, pager, next" :page-size="10"
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
    Receive
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
      let buf = [];
      let filterfriends = [];

      // 检查是否存在 is_friend 属性
      let hasIsFriendProperty = this.friends.length > 0 && this.friends[ 0 ].hasOwnProperty( 'is_friend' );

      if ( hasIsFriendProperty )
      {
        for ( let i = 0; i < this.friends.length; i++ )
        {
          if ( this.friends[ i ].is_friend === true )
          {
            buf.push( this.friends[ i ] );
          }
        }
      } else
      {
        buf = this.friends;
      }

      for ( let i = 0; i < buf.length; i += 10 )
      {
        filterfriends.push( buf.slice( i, i + 10 ) );
      }

      return filterfriends;
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
    },

    handleDelete ( friend )
    {
      ElMessageBox.confirm( '是否删除该好友',
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
        }
      ).then( () =>
      {
        axios.post( 'http://127.0.0.1:8000/api/friend/delete', {
          uid: sessionStorage.getItem( 'uid' ),
          fid: friend.uid,
        } ).then( response =>
        {
          ElMessage( {
            type: 'success',
            message: '删除成功',
          } );

          this.getData();
        } ).catch( error =>
        {
          ElMessage( {
            type: 'error',
            message: '删除失败，请重试',
          } );
        } );
      } ).catch( () =>
      {
        ElMessage( {
          type: 'info',
          message: '你已取消操作',
        } );
      } );
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

    getAvatar ( friend )
    {
      return friend.pic;
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
    },

    handleMenuSelect ( index )
    {
      this.activeTab = index;
    },
  }
}

</script>

<style scoped>
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
</style>
