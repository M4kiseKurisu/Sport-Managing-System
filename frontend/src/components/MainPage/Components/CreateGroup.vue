<template>
  <!-- 点击按钮触发显示对话框 -->
  <el-button type="primary" @click="showDialog = true">Create Group</el-button>

  <!-- el-dialog 标签中使用 showDialog 控制对话框的显示与隐藏 -->
  <el-dialog title="Create Group" :visible.sync="showDialog" width="30%">
    <el-form :model="form" label-width="120px">
      <el-form-item label="团体名称">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="人数上限">
        <el-input v-model="form.max" />
      </el-form-item>
      <el-form-item label="团体简介">
        <el-input v-model="form.description" />
      </el-form-item>
      <el-form-item>
        <!-- 提交按钮 -->
        <el-button type="primary" @click="onSubmit">Create</el-button>
        <!-- 取消按钮 -->
        <el-button @click="showDialog = false">Cancel</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script lang="ts">
import { reactive,ref } from 'vue'

export default {
  setup() {
    const form = reactive({
      name: '',
      max: '',
      description: '',
    })

    // 控制对话框显示与隐藏的变量
    const showDialog = ref(false)

    const onSubmit = () => {
      console.log('submit!')
      // 提交逻辑，可以在这里发送数据到后端等操作
      // 之后可以关闭对话框
      showDialog.value = false
    }

    return {
      form,
      showDialog,
      onSubmit,
    }
  },
}
</script>
