<template>
  <div class="modal">
    <div class="content">
      <div>
        <input
          type="text"
          name="search-box"
          id="search-box"
          v-model="searchTerm"
        />
        <ul v-if="searchResult">
          <li v-for="item in searchResult" :key="item.id">
            <img class="icon" :src="item.icon" :width="44" />
            <span class="name">{{ item.name }}</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="footer">
      <button @click="emits('close', true)">ACCEPT</button>
      <button @click="emits('close', false)">CLOSE</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";

import { searchItem } from "@/utils/item-functions";
import { DictionaryItem } from "@/models/Item";

const emits = defineEmits(["close"]);

const searchTerm = ref<string>("");

const searchResult = ref<DictionaryItem[]>();

watch(searchTerm, (value) => {
  if (!value) {
    searchResult.value = [];
    return;
  }

  searchResult.value = searchItem(value);
});
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.modal {
  @include floating-section;

  .footer {
    display: flex;
    flex-direction: row;
  }
}
</style>
