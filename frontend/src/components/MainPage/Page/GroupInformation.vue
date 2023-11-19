<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
        >
          <el-menu-item index="1" @click="$router.push('/Group/GroupList')">团体中心</el-menu-item>
          <el-menu-item index="2" @click="$router.push('/Group/YourGroup')">你的团体</el-menu-item>
          <el-menu-item index="3" @click="$router.push('/Group/YourApplication')">你的申请</el-menu-item>
          <el-menu-item index="4" @click="$router.push('/Group/PendingReview')">待办审核</el-menu-item>
  </el-menu>
  <div class="h-6" />
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>


</template>

<script lang="ts" setup>
import { ref } from 'vue'

const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>
