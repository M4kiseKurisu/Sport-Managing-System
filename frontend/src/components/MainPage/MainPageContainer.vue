<template>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">
          <Sidebar />
        </el-aside>
        <el-main>
          <!-- <UserInformation /> -->
<<<<<<< HEAD
          <!-- <ActivityInformation /> -->
=======
          <GroupInformation />
>>>>>>> e72df933f9e9f24a2003371097af1e763859b4da
          <!-- <EquipmentBorrow /> -->
          <!-- <EBorrowMain /> -->
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
  
<script>
// 引入 Sidebar 组件
import Sidebar from './SideBar/Sidebar.vue'; // 请替换为实际的路径
import UserInformation from './Page/UserInformation.vue';
import ActivityInformation from './Page/ActivityInformation.vue';
import EquipmentBorrow from './Page/EquipmentBorrow.vue'
<<<<<<< HEAD
import EBorrowMain from './Page/E-Borrow/EBorrowMain.vue'
=======
import FriendInformation from './Page/FriendInformation.vue';
import GroupInformation from './Page/GroupInformation.vue'

>>>>>>> e72df933f9e9f24a2003371097af1e763859b4da

export default {
  components: {
    Sidebar,
    UserInformation,
    ActivityInformation,
    EquipmentBorrow,
<<<<<<< HEAD
    EBorrowMain,
  },
=======
    FriendInformation,
    GroupInformation,
    UserInformation
},
>>>>>>> e72df933f9e9f24a2003371097af1e763859b4da
};
</script>