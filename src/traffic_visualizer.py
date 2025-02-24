import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import pandas as pd


class TrafficVisualizer:
    @staticmethod
    def plot_traffic_characteristics(df, app_name, output_dir):
        """
        Generates histograms for TCP and TLS header fields.
        """
        if df.empty:
            print(f"⚠ No data available to plot for {app_name}.")
            return

        os.makedirs(output_dir, exist_ok=True)

        # Packet Size Distribution
        plt.figure(figsize=(12, 5))
        sns.histplot(df['packet_size'].dropna(), bins=50, kde=True, color='blue')
        plt.title(f'Packet Size Distribution - {app_name}')
        plt.xlabel('Packet Size (Bytes)')
        plt.ylabel('Count')
        plt.savefig(f"{output_dir}/{app_name}_packet_size.png")
        plt.close()

        # TCP Sequence Number Distribution
        if 'tcp_seq' in df.columns and df['tcp_seq'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.histplot(df['tcp_seq'].dropna(), bins=50, kde=True, color='blue')
            plt.title(f'TCP Sequence Number Distribution - {app_name}')
            plt.xlabel('TCP Sequence Number')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.savefig(f"{output_dir}/{app_name}_tcp_seq.png")
            plt.close()

        # TCP Acknowledgment Number Distribution
        if 'tcp_ack' in df.columns and df['tcp_ack'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.histplot(df['tcp_ack'].dropna(), bins=50, kde=True, color='purple')
            plt.title(f'TCP Acknowledgment Number Distribution - {app_name}')
            plt.xlabel('TCP Acknowledgment Number')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.savefig(f"{output_dir}/{app_name}_tcp_ack.png")
            plt.close()

        # TCP Window Size Distribution
        if 'tcp_window' in df.columns and df['tcp_window'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.histplot(df['tcp_window'].dropna(), bins=50, kde=True, color='red')
            plt.title(f'TCP Window Size Distribution - {app_name}')
            plt.xlabel('TCP Window Size')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.savefig(f"{output_dir}/{app_name}_tcp_window.png")
            plt.close()

        # TCP Flags Distribution
        if 'tcp_flags' in df.columns and df['tcp_flags'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.countplot(x=df['tcp_flags'].dropna(), color='orange')
            plt.title(f'TCP Flags Distribution - {app_name}')
            plt.xlabel('TCP Flags (Bit Values)')
            plt.ylabel('Count')
            plt.savefig(f"{output_dir}/{app_name}_tcp_flags.png")
            plt.close()

        # TLS Handshake Type Distribution
        if 'tls_handshake_type' in df.columns and df['tls_handshake_type'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.countplot(x=df['tls_handshake_type'].dropna(), color='green')
            plt.title(f'TLS Handshake Types - {app_name}')
            plt.xlabel('Handshake Type')
            plt.ylabel('Count')
            plt.savefig(f"{output_dir}/{app_name}_tls_handshake.png")
            plt.close()

        # TLS Version Distribution
        if 'tls_version' in df.columns and df['tls_version'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.countplot(x=df['tls_version'].dropna(), color='blue')
            plt.title(f'TLS Versions Used - {app_name}')
            plt.xlabel('TLS Version')
            plt.ylabel('Count')
            plt.savefig(f"{output_dir}/{app_name}_tls_version.png")
            plt.close()

        # TLS Cipher Suites Distribution
        if 'tls_cipher_suite' in df.columns and df['tls_cipher_suite'].dropna().size > 0:
            plt.figure(figsize=(12, 5))
            sns.countplot(y=df['tls_cipher_suite'].dropna(), color='green')
            plt.title(f'TLS Cipher Suites Used - {app_name}')
            plt.xlabel('Count')
            plt.ylabel('TLS Cipher Suite')
            plt.savefig(f"{output_dir}/{app_name}_tls_cipher_suite.png")
            plt.close()

    @staticmethod
    def compare_results(csv_file, output_dir="results/"):
        """
        Generates comparison bar charts from the results CSV file.
        """
        if not os.path.exists(csv_file):
            print("⚠ No comparison CSV file found. Run the analysis first.")
            return

        df = pd.read_csv(csv_file)

        os.makedirs(output_dir, exist_ok=True)

        # Set a larger figure size for readability
        plt.figure(figsize=(12, 6))

        # Compare Average Packet Sizes
        plt.figure(figsize=(10, 5))
        sns.barplot(x="Application", y="Avg_Packet_Size", data=df, palette="Blues_r")
        plt.title("Average Packet Size Comparison")
        plt.ylabel("Packet Size (Bytes)")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, "comparison_packet_size.png"))
        plt.close()

        # Compare TCP Sequence Number Counts
        plt.figure(figsize=(10, 5))
        sns.barplot(x="Application", y="TCP_Seq_Count", data=df, palette="Reds_r")
        plt.title("TCP Sequence Number Count Comparison")
        plt.ylabel("Unique TCP Sequence Numbers")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, "comparison_tcp_seq.png"))
        plt.close()

        # Compare TCP Window Sizes
        plt.figure(figsize=(10, 5))
        sns.barplot(x="Application", y="TCP_Window_Size_Avg", data=df, palette="Greens_r")
        plt.title("Average TCP Window Size Comparison")
        plt.ylabel("Window Size")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, "comparison_tcp_window.png"))
        plt.close()

        # Compare TLS Handshake Counts
        plt.figure(figsize=(10, 5))
        sns.barplot(x="Application", y="TLS_Handshake_Count", data=df, palette="Purples_r")
        plt.title("TLS Handshake Type Count Comparison")
        plt.ylabel("Count of Unique TLS Handshake Types")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, "comparison_tls_handshake.png"))
        plt.close()

        print("✅ Comparison graphs saved in results/ folder.")
