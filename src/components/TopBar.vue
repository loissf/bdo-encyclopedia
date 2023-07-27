<template>
  <div class="item-search">
    <input
      type="text"
      name="search-input"
      id="search-input"
      v-model="searchTerm"
    />
    <button type="button" @click="search">search</button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const searchTerm = ref<string>("");

function search() {
  //
}
</script>
