<template>
  <div class="item-name" :grade="itemGrade">
    <span v-if="enhancement">{{ enhancementName }}: </span>
    <span>{{ itemName }}</span>
  </div>
</template>

<script setup lang="ts">
import { getEnhancementName } from "@/utils/item-functions";
import { computed } from "vue";

const props = defineProps({
  itemId: {
    type: Number,
    required: true,
  },
  itemName: {
    type: String,
    required: true,
  },
  itemGrade: {
    type: Number,
    required: true,
  },
  enhancement: {
    type: Number,
    required: false,
  },
});

const enhancementName = computed(() =>
  getEnhancementName(props.itemId, props.enhancement ?? 0)
);
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.item-name {
  @include item-name;

  text-align: left;
}
</style>
