<template>
  <div class="categories-selector">
    <ul>
      <li v-for="category in menu" :key="category.id.toString()">
        <CollapsibleElement
          :title="category.name"
          :id="(category.id as string)"
          :category-id="(category.id as string)"
          :expanded="expandedCategory"
          @click="expandedCategory = category.id as string"
        >
          <span
            class="subcategory"
            v-for="subcategory in category.subcategories"
            :key="subcategory.id"
            @click="
              selectCategory(category.id as string, subcategory.id as string)
            "
            >{{ subcategory.name }}</span
          >
        </CollapsibleElement>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import market_categories from "@/resources/market_categories.json";
import { useMarketStore } from "@/marketplace/market-store";
import CollapsibleElement from "./CollapsibleElement.vue";

const marketStore = useMarketStore();

const menu = computed(
  (): {
    id: string;
    name: string;
    subcategories: { id: string; name: string }[];
  }[] =>
    Object.entries(market_categories).map((x) => {
      const category = Object.values(x);
      const id = category[0] as string;
      const name = Object.keys(Object.values(x)[1])[0];
      const subcategories = Object.entries(
        Object.values(Object.values(x)[1])[0]
      ).map((x) => ({ id: x[0] as string, name: x[1] as string }));

      return { id, name, subcategories };
    })
);

const expandedCategory = ref<string>("");

async function selectCategory(categoryId: string, subcategoryId: string) {
  marketStore.selectCategory({
    mainCategory: parseInt(categoryId),
    subCategory: parseInt(subcategoryId),
  });
}
</script>

<style scoped lang="scss">
@import "@/styles/main.scss";

.categories-selector {
  overflow-y: auto;
  overflow-x: hidden;
  height: 100%;

  @include custom-scrollbar;

  ul {
    margin: 0;
    padding: 0;

    li {
      display: block;

      .subcategory {
        padding: 0.25rem;
        user-select: none;

        &:hover {
          background-color: rgb(65, 65, 65);
        }
      }
    }
  }
}
</style>
../../marketplace/market-store
