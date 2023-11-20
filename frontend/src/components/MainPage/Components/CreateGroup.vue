<template>
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
    </el-form>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </template>
  
  <script lang="ts" setup>
  import { reactive } from 'vue'
  
  // do not use same name with ref
  const form = reactive({
    name: '',
    max: '',
    description: '',
  })
  
  const onSubmit = () => {
    console.log('submit!')
  }
  </script>
  