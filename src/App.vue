<template>
  <Enhancement></Enhancement>
  <!-- <Marketplace></Marketplace> -->
</template>

<script setup lang="ts">
import Marketplace from "./marketplace/Marketplace.vue";
import Enhancement from "./enhancement/Enhancement.vue";
</script>

<style lang="scss">
#app {
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: #222222;
  margin: 0;
  padding: 0;
  overflow-y: auto;
}
</style>
