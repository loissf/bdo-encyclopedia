<template>
  <div class="icon-wrapper">
    <img class="item-icon" :src="icon" :grade="itemGrade" />
    <img v-if="enhancement" :src="enhancementSymbolIcon" class="symbol-icon" />
  </div>
</template>

<script setup lang="ts">
import { getIconUrl, getEnhancementSymbolIcon } from "@/utils/item-functions";
import { computed } from "vue";

const props = defineProps({
  itemId: {
    type: Number,
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

const icon = computed(() => getIconUrl(props.itemId));

const enhancementSymbolIcon = computed(() =>
  getEnhancementSymbolIcon(props.itemId, props.enhancement ?? 0)
);
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.icon-wrapper {
  position: relative;

  width: 2.75rem;
  height: 2.75rem;

  .item-icon {
    @include item-icon;
    position: absolute;
    top: 0;
    left: 0;

    width: 2.75rem;
    height: 2.75rem;
  }

  .symbol-icon {
    position: absolute;
    top: 0;
    left: 0;

    border: 2px solid transparent;

    width: 2.75rem;
    height: 2.75rem;
  }
}
</style>
