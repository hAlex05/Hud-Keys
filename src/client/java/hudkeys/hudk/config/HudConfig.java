package hudkeys.hudk.config;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import net.fabricmc.loader.api.FabricLoader;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class HudConfig {
    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();
    private static final File CONFIG_FILE = new File(FabricLoader.getInstance().getConfigDir().toFile(), "hudkeys.json");

    // --- Configuration Values ---
    public int xOffset = 0;
    public int yOffset = 0;
    public float scale = 0.6f;
    public boolean showUnpressedKeys = true;

    // --- File Saving/Loading Logic ---
    private static HudConfig instance;

    public static HudConfig getInstance() {
        if (instance == null) {
            load();
        }
        return instance;
    }

    public static void load() {
        if (CONFIG_FILE.exists()) {
            try (FileReader reader = new FileReader(CONFIG_FILE)) {
                instance = GSON.fromJson(reader, HudConfig.class);
            } catch (Exception e) {
                System.err.println("Failed to load Hud Keys config!");
                e.printStackTrace();
            }
        }
        if (instance == null) {
            instance = new HudConfig();
            save();
        } else {
            if (!Float.isFinite(instance.scale) || instance.scale < 0.1f || instance.scale > 3.0f) {
                instance.scale = 0.6f;
            }
        }
    }

    public static void save() {
        try {
            File parent = CONFIG_FILE.getParentFile();
            if (parent != null && !parent.exists()) {
                parent.mkdirs();
            }
            try (FileWriter writer = new FileWriter(CONFIG_FILE)) {
                GSON.toJson(instance, writer);
            }
        } catch (IOException e) {
            System.err.println("Failed to save Hud Keys config!");
            e.printStackTrace();
        }
    }
}
