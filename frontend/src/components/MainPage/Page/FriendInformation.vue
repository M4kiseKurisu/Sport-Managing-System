<template>
  <div>
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
              <el-input v-model="keyword" placeholder="搜索成员"></el-input>
            </div>
            <el-button @click="search" class="searchButton">查询</el-button>
          </div>
        </template>
        <template #default="scope">
          <div v-for="friend in scope.row" :key="friend.uid" class="user-info">
            <el-button size="small" type="danger" @click="handleDelete(friend)">删除好友</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <el-pagination :small="small" :disabled="disabled" :background="background" layout="prev, pager, next" :page-size="10"
      :total="totalPages" v-model:current-page="currentPage" @current-change="handleCurrentChange" />
  </div>
</template>

<script lang="js">
import axios from 'axios'
export default {
  data ()
  {
    return {
      friends: [],
      small: false,
      background: false,
      disabled: false,
      currentPage: 1,
      msg: "",
      defaultImage: "./src/images/group-default-picture.png",
      keyword: "",
    }
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
      let filterfriends = [];

      for ( let i = 0; i < this.friends.length; i += 10 )
      {
        filterfriends.push( this.friends.slice( i, i + 10 ) )
      }
      return filterfriends
    }
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
          console.log( result.data.list )
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
          gid: sessionStorage.getItem( 'uid' ),
          keyword: this.keyword
        }
      } ).then( ( result ) =>
      {
        if ( result.data.status )
        {
          this.friends = result.data.list; // 将后端数据赋值给 Users
          this.msg = result.data.msg;
        }
      } );
    },
    getAvatar ( friend )
    {
      return friend.pic;
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
</style>
