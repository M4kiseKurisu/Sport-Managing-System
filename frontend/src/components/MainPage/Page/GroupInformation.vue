<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-menu
          :default-active="activeIndex"
          mode="horizontal"
          router="true"
        >
          <el-menu-item index="/Page/GroupInformation/GroupList">团体中心</el-menu-item>
          <el-menu-item index="/Page/GroupInformation/YourGroup">你的团体</el-menu-item>
          <el-menu-item index="/Page/GroupInformation/YourApplication">你的申请</el-menu-item>
          <el-menu-item index="/Page/GroupInformation/PendingReview">待办审核</el-menu-item>
        </el-menu>
        <div class="h-6" />
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent} from 'vue'

export default defineComponent({
  data() {
    return {
      activeIndex: "GroupInformation/GroupList"
    }
  },
})
</script>
